from email.iterators import typed_subpart_iterator
import torch
from torch import nn
from d2l import torch as d2l

from assets.articles.mathematics.softmax_fixed import net

n_train,n_test,num_inputs,batch_size=20,100,200,5
true_w,true_b=torch.ones((num_inputs,1))*0.01,0.05
train_data=d2l.synthetic_data(true_w,true_b,n_train)
'''def synthetic_data(w,b,num):
X=d2l.normal(0,1,(num,len(w)))
y=d2l.matmul(X,w)+b
y+=d2l.normal(0,0.01,y.shape)
return X,d2l.reshape(y,(-1,1))
''' 
train_iter=d2l.load_array(train_data,batch_size)
'''
dataset =torch.utils.data.TensorDataset(*data_array)(类似于zip函数))
return torch.utils.data.Dataloader(dataset,batch_size,shuffle=is_train)


torch.normal

mean=3 * n_data：均值是 3，形状与 n_data 相同 ((100,2))。
std=1：标准差是 1，表示数据有一定的随机性。


Dataloader是一个可迭代对象 用iter(dataloader) not next()
创建一个 Dataset 对象
创建一个 DataLoader 对象
循环这个 DataLoader 对象，将数据, label加载到模型中进行训练

'''
test_data=d2l.synthetic_data(true_w,true_b,n_test)
test_iter=d2l.load_array(test_data,batch_size,is_train=False)

def init_params():
    w=torch.normal(0,1,size=(num_inputs,1),requires_grad=True)
    b=torch.zeros(1,requires_grad=True)
    return [w,b]


def l2_penalty(w):
    return torch.sum(w.pow(2))/2

def train(lambd):
    w,b=init_params()
    net,loss=lambda X:d2l.linreg(X,w,b),d2l.squared_loss
    num_epochs,lr =100,0.003
    animator=d2l.Animator(xlabel='epochs',ylabel='loss',yscale='log',xlim=[5,num_epochs],legend=['train','test'])
    for epoch in range(num_epochs):
        for X,y in train_iter:
            #增加L2范数惩罚项
            #广播机制使L2_penalty(w)成为一个长度为batch_size的向量
            l=loss(net(X),y)+lambd*l2_penalty
            l.sum().backward()
            d2l.sgd([w,b],lr,batch_size)
            '''
            def sgd(params,lr,batch_size):
                with torch.no_grad():
                    for param in params:
                        param-=lr*param.grad/batch_size
                        param.grad.zero_()  ##如果不清零,grad属性值会一直叠加
            '''

def train_consise(wd):
    net=nn.Sequential(nn.Linear(num_inputs,1))
    for param in net.parameters:
        param.data.normal_()#normal mean=0，std=1
    loss=nn.MSELoss(reduction='none') ##指定应用于输出的归约方式可选值为 'none'、'mean'、'sum'。'none'：不进行归约。'mean'：输出的和除以输出的元素总数。'sum'：输出的元素求和。'''
    num_epochs,lr=200,0.003
    trainer=torch.optim.SGD([{"params":net[0].weight,'weight_decay':wd},{"params":net[0].bias}],lr=lr)
    return trainer





