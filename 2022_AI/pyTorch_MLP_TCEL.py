# MLP by pyTorch, CPU version
# 4 class : T/C/E/L
# 3 patterns / 1 class
# 2 Layer


import torch

# from torch import tensor
# from torchvision import datasets
# from torchvision.transforms import ToTensor
import torch.nn as nn

# import torch.nn.functional as F

import torch.optim as optim

lrate = 0.1
INDIM = 26
H1DIM = 10
H2DIM = 10
OUTDIM = 4

PTTN_NUM = 12

# x  = np.array([[1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
x = torch.tensor([[1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                   0.0, 0.0, 1.0, 0.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 0.0],  # T-1
                  [1.0, 1.0, 1.0, 1.0, 1.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 1.0,
                   0.0, 0.0, 1.0, 0.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 0.0],  # T-2
                  [1.0, 0.0, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 1.0, 0.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 0.0,
                   0.0, 0.0, 1.0, 0.0, 0.0],  # T-3
                  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 1.0, 1.0, 1.0, 1.0],  # C-1
                  [1.0, 1.0, 1.0, 1.0, 1.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 1.0, 1.0, 1.0, 1.0],  # C-2
                  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 1.0,
                   1.0, 1.0, 1.0, 1.0, 0.0],  # C-3
                  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 1.0, 1.0, 1.0, 1.0],  # E-1
                  [1.0, 0.5, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 1.0, 1.0, 1.0, 1.0],  # E-2
                  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 1.0, 1.0, 1.0, 1.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   0.5, 1.0, 1.0, 1.0, 1.0],  # E-3
                  [1.0, 1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 1.0, 1.0, 1.0, 1.0],  # L-1
                  [1.0, 1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 1.0,
                   1.0, 1.0, 1.0, 1.0, 0.0],  # L-2
                  [1.0, 1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0, 0.0,
                   0.3, 1.0, 1.0, 1.0, 1.0]])  # L-3

# t  = np.array([ [1.0, 0.0, 0.0, 0.0],
yt = torch.tensor([[1.0, 0.0, 0.0, 0.0],
                   [1.0, 0.0, 0.0, 0.0],
                   [1.0, 0.0, 0.0, 0.0],
                   [0.0, 1.0, 0.0, 0.0],
                   [0.0, 1.0, 0.0, 0.0],
                   [0.0, 1.0, 0.0, 0.0],
                   [0.0, 0.0, 1.0, 0.0],
                   [0.0, 0.0, 1.0, 0.0],
                   [0.0, 0.0, 1.0, 0.0],
                   [0.0, 0.0, 0.0, 1.0],
                   [0.0, 0.0, 0.0, 1.0],
                   [0.0, 0.0, 0.0, 1.0]])


class network(nn.Module):  # 네트워크 모델 정의
    def __init__(self, inDim, h1Dim, outDim):
        super(network, self).__init__()
        self.fc1 = nn.Linear(inDim, h1Dim)
        self.fc2 = nn.Linear(h1Dim, outDim)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.fc1(x))  # 히든 1층의 출력
        x = self.sigmoid(self.fc2(x))  # 출력층의 출력
        return x


model = network(INDIM, H1DIM, OUTDIM)

optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

Epochs = 30000


def train():
    for epoch in range(Epochs):
        loss_sum = 0
        for p in range(PTTN_NUM):
            X = x[p]  # 0_1. input()
            Y = yt[p]

            model.zero_grad()  # 0_2. initialize()
            optimizer.zero_grad()

            prediction = model(X)  # 1. forward() 결과 출력

            loss = criterion(prediction, Y.to(torch.float32))  # 2_1. 로스 계산
            loss.backward()  # 2_2. backward(), 로스 역전파

            optimizer.step()  # 3. wgt_upodate(), 웨이트 수정

            loss_sum += loss.item()

        if epoch % 100 == 0:
            print("epoch:", epoch, "tss: {:.3f}".format(loss_sum))
            test()


def test():
    correct = 0
    # 데이터로더에서 하나씩 꺼내 추론
    with torch.no_grad():
        for p in range(PTTN_NUM):
            X = x[p]
            Y = yt[p]
            outputs = model(X)  # 출력 계산
            print("Target:", Y, " / Output:", outputs)


train()
print("Finished the train")
test()
print("Finished the test")
