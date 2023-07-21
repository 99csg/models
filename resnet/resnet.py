import torch
import torch.nn as nn
from torchsummary import summary

class BasicBlock(nn.Module):
    mul = 1
    def __init__(self, in_ch, out_ch, stride, skip=True):
        super().__init__()
        self.in_ch = in_ch
        self.out_ch = out_ch
        self.skip = skip

        self.conv1 = nn.Conv2d(self.in_ch, self.out_ch, kernel_size=3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(self.out_ch)
        self.drop_out = nn.Dropout(0.2)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(self.out_ch, self.out_ch, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(self.out_ch)
        self.skip_connection = nn.Sequential()
        if stride != 1:
            self.skip_connection = nn.Sequential(
                nn.Conv2d(self.in_ch, self.out_ch, kernel_size=1, stride=stride),
                nn.BatchNorm2d(self.out_ch)
            )

    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        #out = self.drop_out(out) # add
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        #out = self.drop_out(out) # add
        if self.skip is True:
            out += self.skip_connection(x)
        out = self.relu(out)
        return out

class BottleNeck(nn.Module):
    mul = 4
    def __init__(self, in_ch, out_ch, stride, skip=True):
        super().__init__()
        self.in_ch = in_ch
        self.out_ch = out_ch
        self.skip = skip

        self.conv1 = nn.Conv2d(self.in_ch, self.out_ch, kernel_size=1, stride=stride)
        self.bn1 = nn.BatchNorm2d(self.out_ch)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(self.out_ch, self.out_ch, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(self.out_ch)
        self.conv3 = nn.Conv2d(self.out_ch, self.out_ch*self.mul, kernel_size=1, stride=1)
        self.bn3 = nn.BatchNorm2d(self.out_ch*self.mul)
        self.skip_connection = nn.Sequential()
        if stride != 1 or self.in_ch != self.out_ch*self.mul:
            self.skip_connection = nn.Sequential(
                nn.Conv2d(self.in_ch, self.out_ch*self.mul, kernel_size=1, stride=stride),
                nn.BatchNorm2d(self.out_ch*self.mul)
            )

    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.drop_out(out) # add
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.drop_out(out) # add
        out = self.relu(out)
        out = self.conv3(out)
        out = self.bn3(out)
        out = self.drop_out(out) # add
        if self.skip is True:
            out += self.skip_connection(x)
        out = self.relu(out)
        return out

class ResNet(nn.Module):
    def __init__(self, block, nc, nclass, skip):
        super().__init__()
        self.in_ch = 64
        self.skip = skip
        self.conv1 = nn.Conv2d(3, self.in_ch, kernel_size=7, stride=2, padding=3)
        self.bn1 = nn.BatchNorm2d(self.in_ch)
        self.max1 = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        self.layers1 = self.make_layer(block, 64, nc[0], stride=1)
        self.layers2 = self.make_layer(block, 128, nc[1], stride=2)
        self.layers3 = self.make_layer(block, 256, nc[2], stride=2)
        self.layers4 = self.make_layer(block, 512, nc[3], stride=2)

        self.avgpool = nn.AdaptiveMaxPool2d((1, 1))
        self.fc = nn.Linear(512*block.mul, nclass)


    def make_layer(self, block, out_ch, nc, stride):
        layers = []
        strides = [stride] + [1]*(nc-1)
        for i in range(nc):
            layers.append(block(self.in_ch, out_ch, stride=strides[i], skip=self.skip))
            self.in_ch = block.mul*out_ch
        return nn.Sequential(*layers)  # unpacking

    def forward(self, x):  # input : (3,224,224)
        x = self.conv1(x)  # (64,112,112)
        x = self.bn1(x)
        x = self.max1(x)  # (64,56,56)
        x = self.layers1(x)  # (64,56,56)
        x = self.layers2(x)  # (128,28,28)
        x = self.layers3(x)  # (256,14,14)
        x = self.layers4(x)  # (512,7,7)
        x = self.avgpool(x)  # (512,1,1)
        x = torch.flatten(x, 1)  # (512,)
        x = self.fc(x)   # (10,)
        return x



#resnet50 = ResNet(BottleNeck, [3, 4, 6, 3], 10, True)
#summary(resnet50, (3, 224, 224))

#resnet18_noskip = ResNet(BasicBlock, [2, 2, 2, 2], 10, False)
#summary(resnet18_noskip, (3, 224, 224))











