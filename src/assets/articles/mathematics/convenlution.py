import torch
from torch import nn
from d2l import torch as d2l

def corr2d(X,K):
    h,w=K.shape
    Y=torch.zeros((X.shape[0]-h+1,X.shape[1]-w+1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i,j]=(X[i:i+h,j:j+w]).sum()
    return Y

class Conv2D(nn.Module):
    def __init__(self,kernal_size):
        super.__init__()
        self.weight=nn.Parameter(torch.rand(kernal_size))
        self.bias=nn.Parameter(torch.zeros(1))

    def forward(self,x):
        return corr2d(x,self.weight)+self.bias

X=torch.ones((6,8))
X[:,2:6]=0

K=torch.tensor([[1.0,-1.0]])

Y=corr2d(X,K)


###学习卷积核

conv2d=nn.Conv2d(1,1,kernal_size=(1,2),bias=False)

X=X.reshape((1,1,6,8))
Y=Y.reshape((1,1,6,7))

lr=3e-2

for i in range(10):
    Y_hat=conv2d(X)
    l=(Y_hat-Y)**2
    conv2d.zero_grad()
    l.sum().backward()
    conv2d.weight.data[:]-=lr*conv2d.weight.grad



def comp_conv2d(conv2d,X):
    X=X.reshape((1,1)+X.shape)
    Y=conv2d(X)
    return Y.reshape(Y.shape[2:])

conv2d=nn.Conv2d(1,1,kernal_size=3,padding=1)
X=torch.rand(size=(8,8))
comp_conv2d(conv2d,X).shape

def corr2d_multi_in(X,K):
    return sum(d2l.corr2d(x,k) for x,k in zip(X,K))


def corr2d_multi_out(X,K):
    return torch.stack([corr2d_multi_in(X,k) for k in K],0)

##解决如果边缘发生改变，整体信息不会太受影响，我们通过平均pooling或者 max
def pool2d(X,pool_size,mode='max'):
    p_h,p_w=pool_size
    Y=torch.zeros((X.shape[0]-p_h+1,X.shape[1]-p_w+1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            if mode == 'max':
                Y[i,j]=X[i:i+p_h,j:j+p_w].max()
            elif mode == 'avg':
                Y[i, j] = X[i: i + p_h, j: j + p_w].mean()
    return Y

X=torch.arange(16,dtype=torch.float32).reshape((1,1,4,4))

pool2d = nn.MaxPool2d(3)
pool2d(X)


net = nn.Sequential(
    nn.Conv2d(1, 6, kernel_size=5, padding=2), nn.Sigmoid(),
    nn.AvgPool2d(kernel_size=2, stride=2),
    nn.Conv2d(6, 16, kernel_size=5), nn.Sigmoid(),
    nn.AvgPool2d(kernel_size=2, stride=2),
    nn.Flatten(),
    nn.Linear(16 * 5 * 5, 120), nn.Sigmoid(),
    nn.Linear(120, 84), nn.Sigmoid(),
    nn.Linear(84, 10))