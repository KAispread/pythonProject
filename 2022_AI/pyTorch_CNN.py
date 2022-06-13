import torch
from torch import tensor
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset

import torchvision
from torchvision import datasets
from torchvision.transforms import ToTensor

import numpy as np
import matplotlib.pyplot as plt

use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")
if device == "cuda":
    torch.cuda.manual_seed_all(777)
print("Running on " ,device)

training_data = datasets.MNIST("data", train=True, download=True, transform=ToTensor())
test_data = datasets.MNIST("data", train=False, download=True, transform=ToTensor())

trainLoader = torch.utils.data.DataLoader(training_data, batch_size=100, shuffle=True, drop_last=False)
testLoader = torch.utils.data.DataLoader(test_data, batch_size=100, shuffle=False, drop_last=True)

class network(nn.Module):
    def __init__(self):
        super(network, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 6, (3, 3), padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 16, (3, 3), padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )

        self.fully_connected = nn.Sequential(
            nn.Linear(16 * 7 * 7, 120),
            nn.Linear(120, 84),
            nn.Linear(84, 10),
        )

    def forward(self, x):
        x = self.conv(x)
        x = x.view(-1, 16 * 7 * 7)
        x = self.fully_connected(x)
        return x


def train():
    for epoch in range(Epochs):
        loss_sum = 0
        for data, target in trainLoader:
            X, y = data.to(device), target.to(device)
            optimizer.zero_grad()
            prediction = model(X)
            loss = criterion(prediction, y)
            loss.backward()
            optimizer.step()
            loss_sum += loss.item()
        print("Epoch = %d / Loss = %f" % (epoch + 1, round(loss_sum / batch_count, 3)))
        test()


def test():
    correct = 0
    with torch.no_grad():
        for data, target in testLoader:
            data, target = data.to(device), target.to(device)
            outputs = model(data)

            _, predicted = torch.max(outputs, 1)
            correct += predicted.eq(target).sum()

    percent = round(float(correct/100), 2)
    print("Accuracy = {}% \n".format(percent))

model = network().to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

Epochs = 2
batch_count = len(trainLoader)

train()


################################### 트레인 데이터를 활용한 추론

with torch.no_grad():
  for data, target in trainLoader:
    X_test, Y_test = data.to(device), target.to(device)  # cross
    prediction = model(X_test)

  correct_prediction = torch.argmax(prediction, 1) == Y_test
  accuracy = correct_prediction.float().mean()
  print('Accuracy:', accuracy.item())

  # r = random.randint(0, len(X_test) - 1)
  r = 10
  X_single_data = X_test[r:r + 1].view(-1, 28 * 28).float().to(device)
  Y_single_data = Y_test[r:r + 1].to(device)

  print('Label: ', Y_single_data.item())
  X_1 = X_single_data.view(1, 1, 28, 28)
  single_prediction = model(X_1)
  print('Prediction: ', torch.argmax(single_prediction, 1).item())

  plt.imshow(torch.Tensor.cpu(X_test[r:r + 1].view(28, 28)), cmap='Greys', interpolation='nearest')
  plt.show()


##################################### 10개의 테스트 데이터 출력
image, label = next(iter(testLoader))

def imshow(img):
  img = img / 2 + 0.5
  npimg = img.numpy()
  fig = plt.figure(figsize=(10, 5))
  plt.imshow(np.transpose(npimg, (1, 2, 0)))
  plt.show()

dataiter = iter(testLoader)
images, lables = dataiter.next()
imshow(torchvision.utils.make_grid(images[:10]))


##################################### 10번째 테스트 데이터 출력
### 2D display CPU version
X_test = test_data.test_data.float()
r = 9

plt.imshow(X_test[r:r + 1].view(28, 28), cmap='Greys', interpolation='nearest')
plt.show()