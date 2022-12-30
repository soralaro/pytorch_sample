import torch
from torch import nn
from torchvision.transforms import  Resize
class Net1(nn.Module):

    def __init__(self):
        super(Net1, self).__init__()
        self.resize = Resize(size=(400,400), interpolation=2)

    def forward(self,x):
        y = self.resize(x)
        return y

net = Net1()
print(net)
model = Net1()
torch.save(model.state_dict(), './net1.pth')
