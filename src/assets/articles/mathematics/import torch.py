
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

device='cuda' if torch.cuda.is_available() else "cpu"
print(device)

LEARNING_RATE=0.1
n_epochs=1000
data=torch.rand(1000,2)*2-1
print(data)
labels =(data.norm(dim=1)>0.7).float().unsqueeze(1)
data=data.to(device)
labels = labels.to(device)



class CircleClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 =nn.Linear(2,20)
        self.layer2= nn.Linear(20,1)
    def forward(self,x): #使对象成为可调用对象
        x=torch.relu(self.layer1(x))
        x=torch.sigmoid(self.layer2(x))
        return x

model =CircleClassifier()
model =model.to(device)
loss_fn=nn.BCELoss()
optimizer=optim.AdamW(model.parameters(),lr=LEARNING_RATE)

for epoch in range (n_epochs):
    optimizer.zero_grad()
    predictions=model(data)#做前馈计算
    loss=loss_fn(predictions,labels) #计算损失函数
    loss.backward() #反向传播
    optimizer.step() #更新模型参数
    if epoch%20 ==0:
        print(f"Epoch {epoch}")

prediction=model(data)

print(prediction)

prediction=prediction.cpu()
plt.scatter(data[:,0],data[:,1],c=(prediction.squeeze()>0.5),cmap="coolwarm")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print(labels)
print(data)
