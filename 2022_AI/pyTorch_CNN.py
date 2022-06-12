import torch
from torch import tensor
from torchvision import datasets
from torchvision.transforms import ToTensor
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset
import matplotlib.pyplot as plt
import random
# MNIST pyplot 으로 그리는 법 (시험 문제)


device = 'cuda' if torch.cuda.is_available() else 'cpu'
# torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)
print(device + " is using")

# MNIST 데이터 set 을 가져옴 (training Data) 'Tensor' 라는 자료 구조로
training_data = datasets.MNIST("data", train=True, download=True, transform=ToTensor())

# MNIST 데이터 set 을 가져옴 (non-traning(test) Data) 'Tensor' 라는 자료 구조로
test_data = datasets.MNIST("data", train=False, download=True, transform=ToTensor())

# 데이터 set 을 묶어 준다 / 한번에 처리 하는 단위 = batch_size
# shuffle 로 데이터를 섞어서 학습 시키는 것이 좋음. drop-last 는 100개씩 가져 오다 남은 데이터를 어떻게 할 것인지 지정. false 는 버린다.
trainLoader = torch.utils.data.DataLoader(training_data, batch_size=100, shuffle=True, drop_last=False)
testLoader = torch.utils.data.DataLoader(test_data, batch_size=100, shuffle=True, drop_last=False)


class network(nn.Module):  # network model define
    def __init__(self):
        super(network, self).__init__()           # network 구조를 잡아주는 init
        self.conv = nn.Sequential(                # 소괄호 안의 메서드가 차례대로 실행됨
            nn.Conv2d(1, 6, (3, 3), padding=1),
            # in_channels = 1, out_channels = 6, kernel_size = 3       output = 28 * 28 * 6   6개의 필터 필터당 3*3 배열
            nn.ReLU(),
            # ReLu 는 음수는 0, 양수는 그대로 표시

            nn.MaxPool2d(2, 2),
            # max 풀링  kernel_size = 2, stride = 2                     output = 14 * 14 * 6 (2*2 라서 기존 28*28이 14*14로 줄어듦)
            nn.Conv2d(6, 16, (3, 3), padding=1),
            # in_channels = 6, out_channels = 16, kernel_size = 3      output = 14 * 14 * 16
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
            # max 풀링  kernel_size = 2, stride = 2                     output =  7 *  7 * 16
        )
        # torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)
        # torch.nn.MaxPool2d( kernel_size , stride = None , padding = 0 , dilation = 1 , return_indices = False , ceil_mode = False )

        self.fully_connected = nn.Sequential(
            nn.Linear(16 * 7 * 7, 120),                 # 1층 레이어  입력층  // 7 * 7 탬플릿 16개를 120개 노드로 만듦
            nn.Linear(120, 84),                         # 2층 레이어  은닉 층 // 128개의 노드를 84개의 노드와 연결
            nn.Linear(84, 10)                           # 3층 레이어  결과 층 //  84개의 노드를 10개의 노드와 연결
        )

    def forward(self, x):                               # 구조를 잡은 network 를 실행 할 때 수행 하는 동작 forward
        x = self.conv(x)
        x = x.view(-1, 16 * 7 * 7)                      # 1차원 전환  (nn.flatten)
        x = self.fully_connected(x)
        return x


def train():
    for epoch in range(Epochs):
        loss_sum = 0
        for data, target in trainLoader:
            X, y = data.to(device), target.to(device)   # cross
            optimizer.zero_grad()                       # 기울기를 0으로
            prediction = model(X)                       # model 에 인스턴스를 삽입하면 결과 출력
            loss = criterion(prediction, y)             # 그 결과를 타겟과 결과를 비교하여, cross 로스 계산
            loss.backward()                             # 로스 역전파
            optimizer.step()                            # 실질적 웨이트 수정
            loss_sum += loss.item()
        print("epoch = %d   loss = %f" % (epoch + 1, round(loss_sum / batch_count, 3)))
        test()


def test():
    correct = 0
    with torch.no_grad():                               # 기울기 구하는 작업 없이 아래 코드를 실행.
        for data, target in testLoader:
            data, target = data.to(device), target.to(device)
            outputs = model(data)                       # 출력 계산
            # test는 back propagation 할 필요가 없으므로 코드에서 제외
            # 추론 계산
            _, predicted = torch.max(outputs, 1)        # 가장 큰 인덱스 위치를 리턴함  @ return value, index
            correct += predicted.eq(target).sum()       # 정답과 일치한 경우 정답 카운트를 증가

    data_num = len(test_data)  # 데이터 총 건수
    print("accuracy = {}/10000\n".format(correct))


model = network().to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)    # gradiant dist 와 유사한 것
criterion = nn.CrossEntropyLoss()

Epochs = 2
batch_count = len(trainLoader)

train()
