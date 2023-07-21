#from google.colab import drive
#drive.mount('/content/drive')

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split

import torchvision
import torchvision.transforms as transforms
import torchvision.models as models

import sys
sys.path.append('drive/MyDrive/mlcs/resnet/')
import resnet

# hyperparameters
BATCH_SIZE = 256
LR = 0.001
EPOCHS = 40
LR_DECAY = 0.1
PROGRESS_INTERVAL = 5
PATIENCE = 10

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

transform_train = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    #transforms.RandomRotation(15), # add
    #transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1), # add
    transforms.ToTensor(),
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
])

train_dataset = torchvision.datasets.CIFAR10(root='./data',train=True,download=True,transform=transform_train)
test_dataset = torchvision.datasets.CIFAR10(root='./data',train=False,download=True,transform=transform_test)

train_size = int(0.9*len(train_dataset))
val_size = len(train_dataset)-train_size

train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)  # 45000
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=True)  # 5000
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)  # 10000

model = resnet.ResNet(resnet.BottleNeck, [3, 4, 6, 3], 10, skip=True)
model.state_dict().keys()
if torch.cuda.is_available() is True:
  model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=LR, momentum=0.9, weight_decay=0.001)
#scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=LR_DECAY)

def train(model, epochs, progress_interval, patience):
    train_loss_list = []
    val_loss_list = []
    best_val_loss = float('inf')
    epochs_no_improve = 0
    for i in range(1, epochs+1):
        train_loss = 0
        total_cnt=0
        correct_cnt = 0
        model.train()

        for batch_i, (data, target) in enumerate(train_loader):  # 156 batches # 175 batches
            if torch.cuda.is_available() is True:
                data, target = data.to(device), target.to(device)

            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()

            if (batch_i+1)%progress_interval==0:
              print(f"Training Epoch:{i}, Batch:{batch_i+1}, Loss:{train_loss/(batch_i+1):.4f}")

        train_loss /= len(train_loader)
        train_loss_list.append(train_loss)
        print(f"Training Epoch:{i}, Average Loss:{train_loss:.4f}")

        #scheduler.step()

        model.eval()
        with torch.no_grad():
            val_loss = 0
            for batch_i, (data, target) in enumerate(val_loader):  # 40 batches
                if torch.cuda.is_available() is True:
                    data, target = data.to(device), target.to(device)

                output = model(data)
                loss = criterion(output, target)
                val_loss += loss.item()
                total_cnt+=target.size(0)
                _,pred_label = torch.max(nn.functional.softmax(output,dim=1),1)
                correct_cnt+=(pred_label==target).sum().item()

            val_loss /= len(val_loader)
            val_loss_list.append(val_loss)
            acu = correct_cnt/total_cnt
            print(f"Validation Epoch:{i}, Average Loss:{val_loss:.4f}, Accuracy:{acu:.4f}")

        if val_loss<best_val_loss:
          best_val_loss = val_loss
          epochs_no_improve=0
        else:
          epochs_no_improve += 1
          if epochs_no_improve == patience:
            print("Early stopped!")
            break

    return model, train_loss_list, val_loss_list

model, train_loss_list, val_loss_list = train(model, EPOCHS, PROGRESS_INTERVAL, PATIENCE)

model_name= 'model50second_ep30_add_drop+aug'
model_path = f'drive/MyDrive/mlcs/resnet/{model_name}.pth'
torch.save(model, model_path)

import csv

with open(f'./loss_{model_name}.csv','w') as file:
  writer = csv.writer(file)
  writer.writerow(['train_loss', 'val_loss'])
  for train_loss, val_loss in zip(train_loss_list, val_loss_list):
    writer.writerow([train_loss, val_loss])

def test(model):
    model.eval()
    with torch.no_grad():
        test_loss = 0
        correct_cnt=0
        total_cnt= 0

        for batch_i, (data, target) in enumerate(test_loader):
            if torch.cuda.is_available() is True:
                data, target = data.to(device), target.to(device)
            total_cnt += target.size(0)
            output = model(data)
            loss = criterion(output, target)
            _, pred_label = torch.max(nn.functional.softmax(output,dim=1),1)
            correct_cnt += (pred_label==target).sum().item()
            test_loss += loss.item()

    total_loss = test_loss/len(test_loader)
    acu = correct_cnt/total_cnt
    print(f"Test Loss:{total_loss}, Accuracy:{acu:.4f}")


test(model)






