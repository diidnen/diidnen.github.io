import math
import numpy as np
import time as time
import torch
import random as random
from d2l import torch as d2l

class Timer:
    def __init__(self):
        self.times=[]
        self.start()

    def start(self):
        self.tik=time.time()

    def stop(self):
        self.times.append(time.time()-self.tik)
        return self.times[-1]
    def avg(self):
        return sum(self.times)/len(self.times)
    def sum(self):
        return sum(self.times)
    def cumsum(self):
        return np.array(self.times).cumsum().tolist()
    
n=10000
a=np.ones([n])
b=np.ones([n])

timer=Timer()
timer.start()
#c=torch.zeros(n)
d=a+b
#for i in range(n):
    #c[i]=a[i]+b[i]
print(f'{timer.stop():.5f} sec')

def normal(x,mu,sigma):
    p=1/math.sqrt(2*math.pi*sigma**2)
    return p*np.exp(-1/(2*sigma**2))

def synthetic_data(w, b, num_examples):  #@save
    """生成y=Xw+b+噪声"""
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))

true_w = torch.tensor([0, 0])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)

#print('features:', features[999],'\nlabel:', labels[0])
d2l.set_figsize()

# 绘制散点图
d2l.plt.scatter(features[:, 1].detach().numpy(), labels.detach().numpy(), s=1)  # s 是散点的大小
d2l.plt.xlabel('Feature 1')  # 添加 x 轴标签
d2l.plt.ylabel('Label')      # 添加 y 轴标签
d2l.plt.title('Scatter Plot of Feature 1 vs Label')  # 添加标题
d2l.plt.show()  # 显示图形

def data_iter(batch_size,features,labels):
    num_examples=len(features)
    indices=list(range(num_examples))
    random.shuffle(indices)
    for i in range(0,num_examples,batch_size):
        batch_indices=torch.tensor(indices[i:min(i+batch_size,num_examples)])
        yield features[batch_indices],labels[batch_indices]

batch_size = 10

for X, y in data_iter(batch_size, features, labels):
    print(X, '\n', y)
    break

w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)


def linreg(X,w,b):
    return torch.matmul(X,w)+b

def squared_loss(y_hat, y):  #@save
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

def sgd(params,lr,batch_size):
    with torch.no_grad():
        for param in params:
            param-=lr*param.grad/batch_size
            param.grad.zero_()

lr=0.03
num_epochs=3
net=linreg
loss=squared_loss

for epoch in range(num_epochs):
    for X,y in data_iter(batch_size,features,labels):
        l=loss(net(X,w,b),y)
        l.sum().backward()
        sgd([w,b],lr,batch_size)
    with torch.no_grad():
        train_l=loss(net(features,w,b),labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')
print(f'w的估计误差: {true_w - w.reshape(true_w.shape)}')
print(f'b的估计误差: {true_b - b}')