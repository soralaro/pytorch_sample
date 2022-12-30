import torch
from torch import nn
from torchvision.transforms import  Resize
from torchvision.transforms  import functional 
from torchvision.transforms.functional import InterpolationMode
import torchvision.transforms.functional as F
class Net1(nn.Module):

#    def __init__(self,size,interpolation=InterpolationMode.BILINEAR, max_size=None, antialias=None):
    def __init__(self):
        super(Net1, self).__init__()
#        self.resize = Resize(size, interpolation, max_size, antialias)

#    def forward(self,x,size):
    def forward(self,x):
#        y=F.resize(x, size=[520, 960])
        y=F.resize(x, size=[x[2],x[3]])
#        y=F.resize(x, size)
        #y = self.resize(x)
        return y

#net = Net1(size=(400,400))
net = Net1()
print(net)
#model = Net1(size=(400,400))
model = Net1()
torch.save(model.state_dict(), './net1.pth')
