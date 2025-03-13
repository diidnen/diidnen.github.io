import math
from operator import matmul
from d2l import torch as d2l
import torch
from torch import nn
from torch.nn import functional as F


#设置参数
def get_params(vocab_size, num_hiddens, device): #有中间层和vocab_size就好了
    num_inputs = num_outputs = vocab_size

    def normal(shape):
        return torch.randn(size=shape, device=device) * 0.01

    # 隐藏层参数
    W_xh = normal((num_inputs, num_hiddens))
    W_hh = normal((num_hiddens, num_hiddens))
    b_h = torch.zeros(num_hiddens, device=device)
    # 输出层参数
    W_hq = normal((num_hiddens, num_outputs))
    b_q = torch.zeros(num_outputs, device=device)
    # 附加梯度
    params = [W_xh, W_hh, b_h, W_hq, b_q]
    for param in params:
        param.requires_grad_(True)
    return params

def init_rnn_state(batch_size, num_hiddens, device):
    return (torch.zeros((batch_size, num_hiddens), device=device), )##我需要num_hiddens和batch_size来初始化matrix

def rnn(inputs,state,params): #这里state指的是过去信息
    #先把param取出来
    W_xh,W_hh,b_h,W_hq,b_q=params
    #再把过去的信息取出来
    answer=[]
    H,=state#state是一个元组，这样就取出一个元素
    #进行计算 隐藏层
    for X in inputs:
        h=torch.tanh(torch.matmul(X,W_xh)+torch.matmul(H,W_hh)+b_h)
        Y=matmul(h,W_hq)+b_q
        answer.append(Y)
    return torch.cat(answer,dim=0),(H,)##列数不变行数变 dim=0

class RNNModelScratch:
    def __init__(self,init_state,forward_fn,num_hidden,vocab_size,device):
        self.params=get_params(num_hidden,device,vocab_size)
        self.vocab_size=vocab_size
        self.init_state=init_state
        self.forward_fn=forward_fn
        self.num_hidden=num_hidden
    
    def __call__(self,X,state):
        X=F.one_hot(X.T,self.vocab_size).type(torch.float32)
        return self.forward_fn(X,self.params,state)

    def begin_state(self,batch_size,device):
        return self.init_state(batch_size, self.num_hidden, device)

num_hiddens = 512
net = RNNModelScratch(50, num_hiddens, d2l.try_gpu(), get_params,
                      init_rnn_state, rnn)
state = net.begin_state(X.shape[0], d2l.try_gpu())
Y, new_state = net(X.to(d2l.try_gpu()), state)
Y.shape, len(new_state), new_state[0].shape


def predict(prefix,num_preds,net,vocab,device):
    state=net.begin_state(batch_size=1,devcie=device)
    output=[vocab[prefix[0]]]
    input=lambda: torch.tensor([output[-1]],device=device).reshape((1,1))
    for y in prefix[1:]:
        _,state=net(input(),state)
        output.append(y)
    for _ in num_preds:
        k,state=net(input(),state)
        output.append(int(y.argmax(dim=1).reshape(1)))
    return ''.join([vocab.idx_to_token[i] for i in output])

def grad_clipping(net,theta):
    if isinstance(net,nn.Module):
        params=[p for p in net.parameters() if p.requires_grad]
    else:
        params=net.params
    norm=torch.sqrt(sum(torch.sum(p.grad**2 for p in params)))
    if norm>theta:
        for param in params:
            param.grad[:]*=theta/norm


  