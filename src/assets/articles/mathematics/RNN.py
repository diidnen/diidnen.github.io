##我们要研究序列，然后我们最终会去考虑p(x_t|,x_{t-1}.....x_1)
##但是我们现在肯定想要想怎么去近似p(x_t|,x_{t-1}.....x_1)因为这里面的数量和t有关，所以万一t很大
##第一种考虑只需要一个固定时间序列
##或者保留对过去的某种总结，隐变量自回归模型
from random import shuffle
from tkinter.messagebox import NO
import matplotlib.pyplot as plt
import torch
from torch import nn
import collections 
import re
from d2l import torch as d2l


T=1000
time=torch.arange(1,T+1,dtype=torch.float32)
x=torch.sin(0.01*time)+torch.normal(0,0.2,(T,))
d2l.plot(time,[x],'time','x',xlim=[1,1000],figsize=(6,3))
tau = 4
features=torch.zeros((T-tau,tau))
for i in range(tau):
    features[:,i]=x[i:T-tau+i]
labels=x[tau:].reshape((-1,1))

batch_size,n_train=16,600
train_iter=d2l.load_array((features[:n_train],labels[:n_train]),batch_size,is_train=True)

def init_weight(m):
    if type(m)==nn.Linear:
        nn.init.xavier_uniform_(m.weight)

def get_net():
    net=nn.Sequential(nn.Linear(4,20),
    nn.ReLU(),
    nn.Linear(20,1)
    )
    net.apply(init_weight)
    return net
# 平方损失。注意：MSELoss计算平方误差时不带系数1/2
loss=nn.MSELoss(reduction='none')

def train(net,train_iter,loss,epochs,lr):
    trainer=torch.optim.Adam(net.parameters(),lr)
    for epoch in range(epochs):
        for X,y in train_iter:
            trainer.zero_grad()
            l=loss(net(X),y)
            l.sum().backward()
            trainer.step()
            
        #print(f'epoch {epoch+1},'
        #f'loss:{d2l.evaluate_loss(net,train_iter,loss):f}'
        #)

net=get_net()
#train(net,train_iter,loss,20,0.01)


onestep_preds=net(features)#在计算图中间，需要截断反向传播的梯度计算时。例如，当计算某个 Tensor 的梯度时，我们希望在此处截断反向传播，而不是将梯度一直传递到计算图的顶部，从而减少计算量和内存占用。此时可以使用 detach() 方法将 Tensor 分离出来。
d2l.plot([time,time[tau:]],[x.detach().numpy(),onestep_preds.detach().numpy()],'time','x',legend=['data','1-step preds'],xlim=[1,1000],figsize=(6,3))
multistep_preds=torch.zeros(T)
multistep_preds[:n_train+tau]=x[:n_train+tau]
for i in range(n_train+tau,T):
    multistep_preds[i]=net(multistep_preds[i-tau:i].reshape((1,-1)))

d2l.plot([time, time[tau:], time[n_train + tau:]],
         [x.detach().numpy(), onestep_preds.detach().numpy(),
          multistep_preds[n_train + tau:].detach().numpy()], 'time',
         'x', legend=['data', '1-step preds', 'multistep preds'],
         xlim=[1, 1000], figsize=(6, 3))


max_steps = 64

features = torch.zeros((T - tau - max_steps + 1, tau + max_steps))
# 列i（i<tau）是来自x的观测，其时间步从（i）到（i+T-tau-max_steps+1）
for i in range(tau):
    features[:, i] = x[i: i + T - tau - max_steps + 1]

# 列i（i>=tau）是来自（i-tau+1）步的预测，其时间步从（i）到（i+T-tau-max_steps+1）
for i in range(tau, tau + max_steps):
    features[:, i] = net(features[:, i - tau:i]).reshape(-1)

steps = (1, 4, 16, 64)
d2l.plot([time[tau + i - 1: T - max_steps + i] for i in steps],
         [features[:, (tau + i - 1)].detach().numpy() for i in steps], 'time', 'x',
         legend=[f'{i}-step preds' for i in steps], xlim=[5, 1000],
         figsize=(6, 3))
#plt.show()

d2l.DATA_HUB['time_machine']=(d2l.DATA_URL+'timemachine.txt','090b5e7e70c295757f55df93cb0a180b9691891a')

def read_time_machine():
    with open(d2l.download('time_machine'),'r') as f:
        lines=f.readlines()
    return [re.sub('[^A-Za-z]+', ' ', line).strip().lower() for line in lines]

lines=read_time_machine()
#print(f'#文本总行数:{len(lines)}')
#print(lines[0])
#print(lines[10])

def tokenize(lines,token='word'):
    if token=='word':
        return [line.split() for line in lines]
    elif token=='char':
        return [list(line) for line in lines]
    else:
        print('错误：未知词元类型：' + token)

tokens = tokenize(lines)
#for i in range(11):
    #print(tokens[i])

class Vocab:
    def __init__(self,tokens=None,min_feq=0,reserved_tokens=None) -> None:
        if tokens is None:
            tokens=[]
        if reserved_tokens is None:
            reserved_tokens=[]
        #按出现频率排序
        counter=count_corpus(tokens)
        self._token_freqs=sorted(counter.items(),key=lambda x:x[1],reverse=True)
        # 未知词元
        self.idx_to_token=['<unk>']+reserved_tokens
        self.token_to_idx={token:idx for idx,token in enumerate(self.idx_to_token)}
        for token,freq in self._token_freqs:
            if freq<min_feq:
                break
            if token not in self.idx_to_token:
                self.idx_to_token.append(token)
                self.token_to_idx[token]=len(self.idx_to_token)-1
            
    def __len__(self):
            return len(self.idx_to_token)
        
    def __getitem__(self,tokens):
            if not isinstance(tokens,(list,tuple)):
                return self.token_to_idx.get(tokens,self.unk) #
            return [self.__getitem__(token) for token in tokens]
    def __tokens__(self,idx):
        if not isinstance(idx, (list, tuple)):
            return self.idx_to_token[idx]
        return [self.idx_to_token[index] for index in idx]



    @property
    def unk(self):
        return 0

    @property
    def token_freqs(self):
        return self._token_freqs





def count_corpus(tokens):
    if len(tokens)==0 or isinstance(tokens[0],list):
        tokens=[token for line in tokens for token in line]
    return collections.Counter(tokens)


vocab=Vocab(tokens)
#print(list(vocab.token_to_idx.items())[0:10])
print(tokens)
#print(len(tokens)) 
for i in [0,10]:
    print('文本:', tokens[i])
    print('索引:', vocab[tokens[i]])

##### 8.3还没看

##现在8.4

