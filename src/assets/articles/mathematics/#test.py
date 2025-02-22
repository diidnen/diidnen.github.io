from turtle import forward
import torch
import torch.nn as nn
from torch.nn import functional as F
import random
import textwrap

# 检查 GPU 是否可用
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 超参数设置
batch_size = 64  # 增加批次大小
block_size = 512  # 增加上下文长度
n_embd = 512  # 增加嵌入维度
wrap_width = 50  # 文本换行宽度
dropout_value = 0.2
num_heads = 16  # 多头注意力头数
n_layer=10

# 设置随机种子
torch.manual_seed(1337)

# 读取文本文件
file_name = r"C:/Users/Devoir/训练文档.txt"
with open(file_name, 'r', encoding='utf-8') as f:
    text = f.read()

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
    x = torch.stack([data[i:i + block_size] for i in ix]).to(device)  # 输入
    y = torch.stack([data[i + 1:i + block_size + 1] for i in ix]).to(device)  # 目标
    return x, y

# Head 类（多头注意力)
class Head(nn.Module):
    def __init__(self, head_size, dropout_value):
        super().__init__()
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.register_buffer("tril", torch.tril(torch.ones(block_size, block_size)))
        self.dropout = nn.Dropout(dropout_value)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)  # (B, T, head_size)
        q = self.query(x)
        wei = q @ k.transpose(-2, -1) * k.shape[-1] ** (-0.5)  # 注意力矩阵
        wei = wei.masked_fill(self.tril == 0, float('-inf'))
        wei = F.softmax(wei, dim=-1)
        wei = self.dropout(wei)
        v = self.value(x)
        out = wei @ v  # (B, T, head_size)
        return out

# 多头注意力机制
class MultiHeadAttention(nn.Module):
    def __init__(self, num_heads, head_size, dropout_value):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size, dropout_value) for _ in range(num_heads)])
        self.proj = nn.Linear(n_embd, n_embd)
        self.dropout = nn.Dropout(dropout_value)

    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        out = self.proj(out)
        out = self.dropout(out)
        return out

# 简单的语言模型

class FeedForward(nn.Module):
    def __init__(self,n_embd):
        super().__init__()
        self.net=nn.Sequential(
            nn.Linear(n_embd, n_embd*4),
            nn.ReLU(),
            nn.Linear(n_embd*4, n_embd),#但是为什么这里n_embd 而不是size 
            nn.Dropout(dropout_value)
        )
    def forward(self,x):
        return self.net(x)

class Block(nn.Module):
    def __init__(self, n_embd, num_heads):
        super().__init__()
        self.sa = MultiHeadAttention(num_heads, n_embd // num_heads, dropout_value)  # 自注意力
        self.ffwd = FeedForward(n_embd)  # 前馈神经网络
        self.ln1 = nn.LayerNorm(n_embd)  # 层归一化 1
        self.ln2 = nn.LayerNorm(n_embd)  # 层归一化 2

    def forward(self, x):
        # 自注意力 + 残差连接
        x = x + self.sa(self.ln1(x))  # ln1 用于自注意力
        # 前馈神经网络 + 残差连接
        x = x + self.ffwd(self.ln2(x))  # ln2 用于前馈神经网络
        return x

class LanguageModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding_table = nn.Embedding(size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size, n_embd)
        self.blocks=nn.Sequential(*[Block(n_embd,num_heads) for _ in range(n_layer)])
        self.ln_f=nn.LayerNorm(n_embd)
        self.lm_head=nn.Linear(n_embd,size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        token_embd = self.token_embedding_table(idx)
        position_idx = torch.arange(T, device=device)
        position_embd = self.position_embedding_table(position_idx)
        x = token_embd + position_embd
        x = self.block(x)
        x = self.ln_f(x)
        logits=self.lm_head(x)
        #logits = torch.relu(self.network1(x))
        #logits = self.network2(logits)
        #为什么是线性
        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B * T, C)
            targets = targets.view(B * T)
            loss = F.cross_entropy(logits, targets)
        return logits, loss

    def generate(self, token_sequ, max_new_tokens):
        # Move token_sequ to the same device as the model
        token_sequ = token_sequ.to(device)  # Add this line
        for _ in range(max_new_tokens):
            tokens_input = token_sequ[:, -block_size:].to(device)
            logits, loss = self.forward(tokens_input)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            token_next = torch.multinomial(probs, num_samples=1)
            token_sequ = torch.cat((token_sequ, token_next), dim=1)
        return token_sequ

# 运行模型
def main():
    print(f"训练内容: {file_name}")
    max_new_tokens = 500
    start_idx = random.randint(0, len(val_data) - block_size - max_new_tokens)
    model = LanguageModel().to(device)

    # 设定优化器
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.0003)

    # 训练循环
    for i in range(200):
        xb, yb = get_batch("train")
        logits, loss = model(xb, yb)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
        if i % 100 == 0:
            print(f"Step {i}, Loss: {loss.item()}")

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

if __name__ == "__main__":
    main()