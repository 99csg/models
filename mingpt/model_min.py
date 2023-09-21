import math

import torch
import torch.nn as nn
from torch.nn import functional as F

from utils import CfgNode as CN


class NewGELU(nn.Module):
    """GELU activation function"""
    def forward(self, x):
        return 0.5*x*(1.0+torch.tanh(math.sqrt(2.0/math.pi)*(x+0.044715*torch.pow(x,3.0))))


class CasualSelfAttention(nn.Module):
    """multi-head masked self-attention layer with projection at the end"""
    def __init__(self, config):
        super().__init__()
        assert config.n_embd % config.n_head == 0
        self.c_attn = nn.Linear(config.n_embd, 3*config.n_embd)  # key, query, value projections
        self.c_proj = nn.Linear(config.n_embd, config.n_embd)  # projection
        self.attn_dropout = nn.Dropout(config.attn_pdrop)
        self.resid_dropout = nn.Dropout(config.resi_pdrop)
        self.register_buffer("bias", torch.tril(torch.ones(config.block_size, config.block_size))
                             .view(1,1,config.block_size, config.block_size))
        self.n_heads = config.n_head
        self.n_embd = config.n_embd

    def forward(self, x):
        B, T, C = x.size()  # batch_size, sequence length, n_embd(embed dim)

        q, k, v = self.c_attn(x).split(self.n_embd, dim=2)
        k = k.view(B,T,self.n_heads, C//self.n_heads).transpose(1,2)
        q = q.view(B, T, self.n_heads, C // self.n_heads).transpose(1, 2)
        v = v.view(B, T, self.n_heads, C // self.n_heads).transpose(1, 2)

        att = (q@k.transpose(-2,-1))*(1.0/math.sqrt(k.size(-1)))
        att = att.masked_fill(self.bias[:,:,:T,:T]==0, float('-inf'))
        att = F.softmax(att,dim=-1)
        att = self.attn_dropout(att)
        y = att@v
        y = y.transpose(1,2).contiguous().view(B,T,C)

        y=self.resid_dropout(self.c_proj(y))
        return y


class Block(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.ln_1 = nn.LayerNorm(config.n_embd)
        self.attn = CasualSelfAttention(config)
        self.ln_2 = nn.LayerNorm(config.n_embd)
        self.mlp = nn.ModuleDict(dict(
            c_fc=nn.Linear(config.n_embd, 4*config.n_embd),
            c_proj=nn.Linear(4*config.n_embd, config.n_embd),
            act=NewGELU(),
            dropout=nn.Dropout(config.resi_pdrop)
        ))
        m = self.mlp
        self.mlpf = lambda x:m.dropout(m.c_proj(m.act(m.c_fc(x))))

    def forward(self, x):
        x = x+self.attn(self.ln_1(x))
        x = x+self.mlpf(self.ln_2(x))
        return x


class GPT(nn.Module):

    @staticmethod
    def get_default_config():
        C = CN()
        C.model_type = 'gpt'
        C.n_layer = None
        C.n_head = None
        C.n_embd = None
        C.vocab_size = None
        C.block_size = None
        C.embd_pdrop = 0.1
        C.resi_pdrop = 0.1
        C.attn_pdrop = 0.1
        return C

    def __init__(self, config):
        super().__init__()
        assert config.vocab_size is not None
        assert config.block_size is not None
        self.block_size = config.block_size

        type_given = config.model_type is not None
        params_given = all([config.n_layer is not None, config.n_head is not None, config.n_embd is not None])

        assert type_given ^ params_given  # XOR 하나만 1일 때 True 반환
        if type_given:
            config.merge_from_dict({
                'openai-gpt':dict(n_layer=12,n_head=12,n_embd=768),
                'gpt2': dict(n_layer=12, n_head=12, n_embd=768),
                'gpt2-medium': dict(n_layer=24, n_head=16, n_embd=1024),
                'gpt2-large': dict(n_layer=36, n_head=20, n_embd=1280),
                'gpt2-xl': dict(n_layer=48, n_head=25, n_embd=1600),
                'gopher-44m': dict(n_layer=8,n_head=16,n_embd=512),
                'gpt-mini': dict(n_layer=6, n_head=6, n_embd=192),
                'gpt-micro': dict(n_layer=4, n_head=4, n_embd=128),
                'gpt-nano': dict(n_layer=3, n_head=3, n_embd=48),
            }[config.model_type])

        self.transformer = nn.ModuleDict(dict(
            wte=nn.Embedding(config.vocab_size, config.n_embd),
            wpe=nn.Embedding(config.block_size, config.n_embd),
            drop=nn.Dropout(config.embd_pdrop),
            h=nn.ModuleList([Block(config) for _ in range(config.n_layer)]),
            ln_f=nn.LayerNorm(config.n_embd),
        ))
        self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False)

        # init weights
        self.apply(self._init_weights)
        for pn, p in self.named_parameters():  # pn:weight or bias, p:parameters
            if pn.endswith('c_proj.weight'):
                torch.nn.init.normal_(p,mean=0.0,std=0.02/math.sqrt(2*config.n_layer))

        n_params = sum(p.numel() for p in self.transformer.parameters())
        print("number of parameters:%.2fM" % (n_params/1e6))

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight,mean=0.0,std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight,mean=0.0,std=0.02)
        elif isinstance(module, nn.LayerNorm):
            torch.nn.init.zeros_(module.bias)
            torch.nn.init.ones_(module.weight)

    @classmethod
    def from_pretrained(cls, model_type):
        """from huggingface/transformers checkpoint"""
        assert model_type in {'gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl'}
        from transformers import GPT2LMHeadModel

        config = cls.get_default_config()
        config.model_type = model_type
        config.vocab_size=50257
        config.block_size=1024
        model = GPT(config)
        sd = model.state_dict()

        model_hf = GPT2LMHeadModel.from_pretrained(model_type)
        sd_hf = model_hf.state_dict()

        keys = [k for k in sd_hf if not k.endswith('attn.masked_bias')]
        transposed = ['attn.c_attn.weight','attn.c_proj.weight','mlp.c_fc.weight','mlp.c_proj.weight']
        assert len(keys) == len(sd)
        for k in keys:
            if any(k.endswith(w) for w in transposed):
                assert sd_hf[k].shape[::-1]==sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k].t())  # copy parameters from huggingface with transpose
            else:
                assert sd_hf[k].shape == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k])  # copy other parameters

        return model

    def configure_optimizers(self, train_config):
        """parameters for weight decay regularization"""
        decay = set()
        no_decay = set()
        whitelist_weight_modules = (torch.nn.Linear,)
        blacklist_weight_modules = (torch.nn.LayerNorm, torch.nn.Embedding)
        for mn, m in self.named_modules():  # class안에 module이름:mn, nn.Conv2d:m
            for pn, p in m.named_parameters():  # pn:weight or bias, p:parameters
                fpn = '%s.%s' %(mn,pn) if mn else pn

                if pn.endswith('bias'):
                    no_decay.add(fpn)
                elif pn.endswith('weight') and isinstance(m, whitelist_weight_modules):
                    decay.add(fpn)
                elif pn.endswith('weight') and isinstance(m, blacklist_weight_modules):
                    no_decay.add(fpn)

        # check if every parameters are considered
        param_dict= {pn:p for pn, p in self.named_parameters()}
        inter_params = decay & no_decay
        union_params = decay | no_decay
        assert len(inter_params) == 0, "parameters %s made it into both decay/no_decay sets!" % (str(inter_params), )
        assert len(
            param_dict.keys() - union_params) == 0, "parameters %s were not separated into either decay/no_decay set!" \
                                                    % (str(param_dict.keys() - union_params),)

        optim_groups = [
            {'params':[param_dict[pn] for pn in sorted(list(decay))], 'weight_decay':train_config.weight_decay},
            {'params':[param_dict[pn] for pn in sorted(list(no_decay))], 'weight_decay': 0},
        ]

        optimizer = torch.optim.AdamW(optim_groups, lr=train_config.learning_rate, betas=train_config.betas)
        return optimizer

    def forward(self, idx, targets=None):
        device = idx.device
        b, t = idx.size()  # b_s, 8
        assert t <= self.block_size, f"Cannot forward sequence of length {t}, block size is only {self.block_size}"
        pos = torch.arange(0, t, dtype=torch.long, device=device).unsqueeze(0)  # (1,t)

        tok_emb = self.transformer.wte(idx)  # (b,t,c)
        pos_emb = self.transformer.wpe(pos)  # (1,t,c)

        x = self.transformer.drop(tok_emb+pos_emb)
        for block in self.transformer.h:
            x = block(x)
        x = self.transformer.ln_f(x)
        logits = self.lm_head(x)

        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=-1)

        return logits, loss  # (b_s, s_len, vocab_size)

    @torch.no_grad()
    def generate(self, idx, max_new_tokens, temperature=1.0, do_sample=False, top_k=None):
        """inference, iteratively predict new tokens """
        for _ in range(max_new_tokens):  # 한 문장의 단어 개수 만큼 iteration - 다음 단어 예측 모델
            idx_cond = idx if idx.size(1) <= self.block_size else idx[:, -self.block_size:]  # 4 <= 8
            logits, _ = self(idx_cond)  # idx_cond : (b_s, x(=6, want to inference))
            logits = logits[:, -1, :]/temperature  # s_len 마지막 뽑아내기 output dim : (b_s, 6, vocab_size) -> (b_s, 1, vocab_size)

            if top_k is not None:
                v, _ = torch.topk(logits, top_k)
                logits[logits < v[:, [-1]]] = -float('Inf')

            probs = F.softmax(logits, dim=-1)

            if do_sample:
                idx_next = torch.multinomial(probs, num_samples=1)
            else:
                _, idx_next = torch.topk(probs, k=1, dim=-1)  # softmax 가장 큰 것의 인덱스 를 받아옴 (b_s,1)
            idx = torch.cat((idx, idx_next), dim=1)  # output : (b_s, 7)

        return idx  # output : (b_s, 12)







