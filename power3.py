import torch
from torch import nn
class Net1(nn.Module):

#    def __init__(self,size,interpolation=InterpolationMode.BILINEAR, max_size=None, antialias=None):
    def __init__(self):
        super(Net1, self).__init__()
#        self.resize = Resize(size, interpolation, max_size, antialias)

#    def forward(self,x,size):
    def forward(self,x):
        y = torch.pow(x,1.0)
        return y

#net = Net1(size=(400,400))
net = Net1()
print(net)
#model = Net1(size=(400,400))
model = Net1()
torch.save(model.state_dict(), './power3.pth')
