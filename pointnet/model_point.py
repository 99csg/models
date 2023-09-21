import torch
import torch.nn as nn
import torch.nn.functional as F


class InputTransformNet(nn.Module):
    def __init__(self, dim=3):
        super(InputTransformNet, self).__init__()
        self.dim = dim
        self.mlp1 = nn.Sequential(
            nn.Conv2d(dim, 64, kernel_size=1), nn.BatchNorm2d(64), nn.ReLU()
        )
        self.mlp2 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=1), nn.BatchNorm2d(128), nn.ReLU()
        )
        self.mlp3 = nn.Sequential(
            nn.Conv2d(128, 1024, kernel_size=1), nn.BatchNorm2d(1024), nn.ReLU()
        )

        self.maxpooling = nn.MaxPool1d(kernel_size=1024)

        self.fc1 = nn.Sequential(
            nn.Linear(1024, 512), nn.BatchNorm1d(512), nn.ReLU()
        )
        self.fc2 = nn.Sequential(
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU()
        )
        self.transform = nn.Linear(256, 3*dim)

        self.transform.bias.data[0:3 * dim:4] = 1.0
        self.transform.bias.data[1:3 * dim:4] = 0.0
        self.transform.bias.data[2:3 * dim:4] = 0.0

    def forward(self, x):
        """input : (b_s, 3, n, 1)
           output : (b_s, 3, 3)  """
        x = self.mlp1(x)
        x = self.mlp2(x)
        x = self.mlp3(x).squeeze(-1).transpose(-1,-2)  # (b_s,n,1024)
        x = self.maxpooling(x).squeeze(-1)  # (b_s,1024)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.transform(x)  # (b_s,3*n(=3*3))
        x = x.view(-1, 3, self.dim)
        #print(x.shape)
        return x


class FeatureTransformNet(nn.Module):
    def __init__(self, dim=64):
        super(FeatureTransformNet, self).__init__()
        self.dim = dim
        self.mlp1 = nn.Sequential(
            nn.Conv2d(dim, 64, kernel_size=1), nn.BatchNorm2d(64), nn.ReLU()
        )
        self.mlp2 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=1), nn.BatchNorm2d(128), nn.ReLU()
        )
        self.mlp3 = nn.Sequential(
            nn.Conv2d(128, 1024, kernel_size=1), nn.BatchNorm2d(1024), nn.ReLU()
        )

        self.maxpooling = nn.MaxPool1d(kernel_size=1024)

        self.fc1 = nn.Sequential(
            nn.Linear(1024, 512), nn.BatchNorm1d(512), nn.ReLU()
        )
        self.fc2 = nn.Sequential(
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU()
        )
        self.transform = nn.Linear(256, dim*dim)

    def forward(self, x):
        """input : (b_s, 64, n, 1)
           output : (b_s, 64, 64)  """
        inputs = x
        x = self.mlp1(x)
        x = self.mlp2(x)
        x = self.mlp3(x).squeeze(-1).transpose(-1, -2)  # (b_s,n,1024)
        x = self.maxpooling(x).squeeze(-1)  # (b_s,1024)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.transform(x)  # (b_s,dim*dim(=64*64))

        idt = torch.eye(self.dim, dtype=torch.float32).flatten().unsqueeze(0).repeat(x.size()[0],1)
        idt = idt.to(inputs.device)
        x = x+idt
        x = x.view(-1, self.dim, self.dim)
        return x


class PointNet(nn.Module):
    def __init__(self, n, classes, task, device):
        super(PointNet, self).__init__()
        self.n = n
        self.classes = classes
        self.task = task
        self.device = device
        self.input_tnet = InputTransformNet()
        self.feature_tnet = FeatureTransformNet()
        self.weights1 = nn.Parameter(torch.eye(3, device=device))
        self.weights1 = nn.Parameter(torch.eye(64, device=device))

        self.mlp1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=1), nn.BatchNorm2d(64), nn.ReLU()
        )
        self.mlp2 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=1), nn.BatchNorm2d(64), nn.ReLU()
        )
        self.mlp3 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=1), nn.BatchNorm2d(64), nn.ReLU()
        )
        self.mlp4 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=1), nn.BatchNorm2d(128), nn.ReLU()
        )
        self.mlp5 = nn.Sequential(
            nn.Conv2d(128, 1024, kernel_size=1), nn.BatchNorm2d(1024), nn.ReLU()
        )
        self.maxpooling = nn.MaxPool1d(kernel_size=n)

        self.fc1 = nn.Linear(1024, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, classes)

        self.dropout = nn.Dropout(p=0.3)

    def forward(self, x):
        """INPUT : (B_S, N points, 3)
           OUTPUT : (B_S, num_classes) """
        x = x.unsqueeze(-1).permute(0,2,1,3)  # (b_s,3,n,1)
        tnet_output1 = self.input_tnet(x)  # (b_s,3,3)
        x = torch.matmul(x.squeeze(-1).permute(0,2,1), tnet_output1)  # (b_s,n,3)

        x = x.unsqueeze(-1).permute(0, 2, 1, 3)  # (b_s,3,n,1)
        x = self.mlp1(x)  # (b_s, 64, n, 1)
        x = self.mlp2(x)  # (b_s, 64, n, 1)

        tnet_output2 = self.feature_tnet(x)  # (b_s,64,64)
        x = torch.matmul(x.squeeze(-1).permute(0,2,1),tnet_output2)  # (b_s,n,64)

        x = x.unsqueeze(-1).permute(0, 2, 1, 3)  # (b_s,64,n,1)
        x = self.mlp3(x)  # (b_s,64,n,1)
        x = self.mlp4(x)  # (b_s,128,n,1)
        x = self.mlp5(x).squeeze(-1)  # (b_s,1024,n)
        x = self.maxpooling(x.transpose(-2, -1)).squeeze(-1)  # (b_s,1024)
        x = self.fc1(x)  # (b_s,512)
        x = self.dropout(x)
        x = self.fc2(x)  # (b_s,256)
        x = self.dropout(x)
        x = self.fc3(x)  # (b_s,10)
        return x


x = torch.randn(64,1024,3)
test_model = PointNet(1024,10,'classification',device='cpu')
x = test_model(x)
print(x.shape)

