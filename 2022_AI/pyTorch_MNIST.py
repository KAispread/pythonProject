import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch import tensor
from torchvision import datasets  # torchvision --> 영상을 처리하기 좋게 변환하는 것을 모아놓은 라이브러리 // datasets이라는 곳에 MNIST가 있음
from torchvision.transforms import ToTensor  # torchvision.transforms --> 영상의 위치, 회전

# -*- coding: utf-8 -*-
"""torchMNIST_modelNN_GPU.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13VdigVUf7GItzyFu1rH6vNBn-fSUj54e
"""

# -*- coding: utf-8 -*-
"""3층 mlp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uF2rfs4FvBFGummqv4yHbSx9bYQMwPYI
"""


"""
MNIST란 테스트 이미지를 28x28픽셀로 변환된 데이터의 집합이다. 
"""

training_data = datasets.MNIST("data", train=True, download=True, transform=ToTensor())   # MNIST 데이터 (train data)를 불러옴, tensor 자료형으로 변환해서 저장
test_data = datasets.MNIST("data", train=False, download=True, transform=ToTensor())    #  test data를 불러옴

trainLoader = torch.utils.data.DataLoader(training_data, batch_size=64, shuffle=True, drop_last=False)
testLoader = torch.utils.data.DataLoader(test_data, batch_size=64, shuffle=True, drop_last=False)

yt = tensor([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
temp = len(trainLoader)
print(temp)

class network(nn.Module):  # 네트워크 모델 정의
    def __init__(self, in_f1, in_f2, in_f3, out_f):
        super(network, self).__init__()
        self.fc1 = nn.Linear(in_f1, in_f2)  # in_features=784, out_features=300, bias=True
        self.fc2 = nn.Linear(in_f2, in_f3)  # in_features=300, out_features=100, bias=True
        self.fc3 = nn.Linear(in_f3, out_f)  # in_features=100, out_features=10,  bias=True
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = x.view(-1, 28 * 28)  # 1차원 행렬로 변환
        x1 = self.sigmoid(self.fc1(x))  # 히든 1층의 출력
        x2 = self.sigmoid(self.fc2(x1))  # 히든 2층의 출력
        x3 = self.sigmoid(self.fc3(x2))  # 출력층의 출력
        return x3

if torch.cuda.is_available():
    device = torch.device("cuda:0")
    print("running on the GPU")
else:
    device = torch.device("cpu")
    print("running on the CPU")

model = network(784, 300, 100, 10)  # .to(device)
model.to(device)

Epochs = 3

#optimizer = optim.SGD(model.parameters(), lr=0.01)
optimizer = optim.Adam(params=model.parameters(), lr=0.01)
criterion = nn.MSELoss()
batch_count = len(trainLoader)


def train():
    for epoch in range(Epochs):
        loss_sum = 0
        for data, target in trainLoader:
            X, y = data.to(device), yt[target].to(device)
            #model.zero_grad()
            optimizer.zero_grad()

            prediction = model(X)  # 1. forward

            loss = criterion(prediction, y.to(torch.float32))  # 2_1 Loss
            loss.backward()  # 2_2. backpropagation

            optimizer.step()  # 3. update weight

            loss_sum += loss.item()
        print("epoch :", epoch)
        print("loss = " + str(round(loss_sum / batch_count, 3)))
        #if epoch%5 == 0 :
           #test()

def test():
    correct = 0
    # 데이터로더에서 하나씩 꺼내 추론
    with torch.no_grad():
        for data, target in testLoader:
            data, target = data.to(device), target.to(device)
            outputs = model(data.view(-1, 784))  # prediction

            # 정확성 판정
            predicted = torch.max(outputs, dim=1)[1]  # 가장 큰 인덱스 위치를 리턴함  @ return value, index
            correct += predicted.eq(target).sum()  # 정답과 일치한 경우 정답 카운트를 증가
            #print("Target:", target, "Output:", predicted)

    data_num = len(test_data)  # 데이터 총 건수
    print('Accurancy : ({:.3f}%)\n'.format(correct / 100))

fc1 = nn.Linear(784, 20)
sigmoid = nn.Sigmoid()

print(fc1)
print(sigmoid)

for data, target in trainLoader:
            X, y = data.to(device), yt[target].to(device)
x = X.view(-1, 28 * 28)  # 1차원 행렬로 변환

x = sigmoid(fc1(x))  # 히든 1층의 출력
print(x)

train()

test()
