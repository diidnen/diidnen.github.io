from cmath import inf
from lib2to3.pgen2 import token
from multiprocessing import context
from operator import mod
from time import process_time_ns
from turtle import forward, position
import torch
import torch.nn as nn
from torch.nn import functional as F
import random
import textwrap

# 超参数设置
batch_size = 8  # 同时处理的样本数
block_size = 125  # 上下文长度（调整为 5 个字）
n_embd = 16  # 嵌入维度
wrap_width = 50  # 文本换行宽度 
dropout_value=0.2

# 设置随机种子
torch.manual_seed(1337)

# 读取文本文件
file_name = r'C:\Users\Devoir\训练文档.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    text = f.read()
    ##print("原始文本：")
    ##print(text)

# 获取所有字符并排序
chars = sorted(list(set(text)))
size = len(chars)

# 创建字符到索引和索引到字符的映射
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s]  # 编码：字符串 -> 数字列表
decode = lambda l: "".join([itos[i] for i in l])  # 解码：数字列表 -> 字符串

# 将文本编码为张量
data = torch.tensor(encode(text), dtype=torch.long)

# 划分训练集和验证集
n = int(0.9 * len(data))  # 前 90% 用于训练
train_data = data[:n]
val_data = data[n:]

# 获取批次数据
def get_batch(split):
    data = train_data if split == "train" else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    
    x = torch.stack([data[i:i + block_size] for i in ix])  # 输入
    y = torch.stack([data[i + 1:i + block_size + 1] for i in ix])  # 目标
    return x, y

#Head 类（多头注意力)
class Head(nn.Module):
    def __init__(self,head_size,dropout_value):
        super().__init__()
        self.key = nn.Linear(n_embd,head_size,bias=False)
        self.query = nn.Linear(n_embd,head_size,bias=False)
        self.value = nn.Linear(n_embd,head_size,bias=False)
        self.register_buffer("tril",torch.tril(torch.ones(block_size,block_size))) #矩阵下三角的值不变(比如股票预测续写下文（我们不能得知后面的信息），不用的时候比如总结，比如翻译)
        self.dropout=nn.Dropout(dropout_value)
    def forward(self,x):
        B,T,C =x.shape
        k=self.key(x)#(B,T,head_size)
        q=self.query(x)

        wei=   q @ k.transpose(-2,-1) *k.shape[-1]**(0.5)#torch.ones(block_size,block_size)#注意力矩阵
        wei=wei.masked_fill(self.tril==0,-inf)
        wei=F.softmax(wei,dim=-1)
        wei=self.dropout(wei)##这一步的作用
        v=self.value(x)
        out=wei@ v #(T,head_size)
        return out



# 简单的语言模型
class LanguageModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding_table=nn.Embedding(size,n_embd)
        self.position_embedding_table=nn.Embedding(block_size,n_embd)
        self.head=Head(n_embd,dropout_value)
        self.network1=nn.Linear(n_embd,500)
        self.network2=nn.Linear(500,size)
        

    def forward(self, idx, targets=None):
        B, T = idx.shape  # B = batch_size, T = block_size
        token_embd=self.token_embedding_table(idx)
        position_idx=torch.arange(block_size)
        position_embd=self.position_embedding_table(position_idx)
        x=token_embd+position_embd##为什么相加
        head_out=self.head(x)
        logits=torch.relu(self.network1(head_out))
        logits=self.network2(logits)
        
        ##random_tensor = torch.rand(B, T, size)  # 随机生成 logits
        ##logits = random_tensor / random_tensor.sum(dim=-1, keepdim=True)  # 归一化
        if targets is None:
            loss = None
        else:
            B,T,C=logits.shape
            logits=logits.view(B*T,C) #摊平
            targets=targets.view(B*T)
            loss=F.cross_entropy(logits,targets)
        return logits, loss

    def generate(self, token_sequ, max_new_tokens):
        for _ in range(max_new_tokens):
            tokens_input = token_sequ[:, -block_size:]  # 只使用最后 block_size 个 token
            logits, loss = self.forward(tokens_input)
            logits = logits[:, -1, :]  # 取最后一个时间步的 logits
            probs = F.softmax(logits, dim=-1)  # 转换为概率分布
            token_next = torch.multinomial(probs, num_samples=1)  # 采样下一个 token
            token_sequ = torch.cat((token_sequ, token_next), dim=1)  # 将新 token 添加到序列中
        new_tokens = token_sequ[:, -max_new_tokens:]  # 只返回新生成的 token
        return new_tokens

# 运行模型
def main():
    print(f"训练内容:{file_name}")
    max_new_tokens = 500  # 生成 10 个新字符
    start_idx = random.randint(0, len(val_data) - block_size - max_new_tokens)  # 随机选择起始位置
    model = LanguageModel()

    #设定一个优化器
    optimizer=torch.optim.AdamW(model.parameters(),lr=0.0003)

    #训练循环
    for i in range(500):
        #取样
        xb,yb=get_batch("train")
        logits,loss=model(xb,yb) #前馈运算
        optimizer.zero_grad(set_to_none=True)#把旧梯度归零
        loss.backward() #反向传播，计算新的梯度
        optimizer.step() #更新模型参数

    # 上文内容
    context = torch.zeros((1, block_size), dtype=torch.long)
    context[0, :] = val_data[start_idx:start_idx + block_size]
    context_str = decode(context[0].tolist())
    wrapped_context_str = textwrap.fill(context_str, width=wrap_width)

    # 真实下文
    real_next_tokens = torch.zeros((1, max_new_tokens), dtype=torch.long)
    real_next_tokens[0, :] = val_data[start_idx + block_size:start_idx + block_size + max_new_tokens]
    real_next_tokens_str = decode(real_next_tokens[0].tolist())
    wrapped_real_next_str = textwrap.fill(real_next_tokens_str, width=wrap_width)

    # 生成下文
    generated_tokens = model.generate(context, max_new_tokens)
    generated_str = decode(generated_tokens[0].tolist())
    wrapped_generated_str = textwrap.fill(generated_str, width=wrap_width)

    # 打印结果
    print("上文内容：")
    print(wrapped_context_str)
    print("\n生成的下文：")
    print(wrapped_generated_str)
    print("\n真实的下文：")
    print(wrapped_real_next_str)


#执行

main()
#head=Head(5)
#print(head.tril)
#wei=torch.ones(block_size,block_size)#注意力矩阵

#wei=wei.masked_fill(head.tril==0,-inf)
#wei=F.softmax(wei,dim=-1)
#print(wei)



##print(data)

##print(stoi)
#print(chars)
#print(encode)

#x,y=get_batch("train")
#print(x)

#model=LanguageModel()
#out=model(x)
#print(out)


##print(get_batch("train"))

##token_embedding_table=nn.Embedding(size,n_embd)
##embd=token_embedding_table(x)

##position_embedding_table=nn.Embedding(block_size,n_embd)
##position_idx=torch.arange(block_size)
##position_embd=position_embedding_table(position_idx)
##print(embd)
##print(position_idx)
##print(position_embd)