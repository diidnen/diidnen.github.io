import torch
from torch import nn
from d2l.torch import *

batch_size, num_steps = 32, 35
train_iter, vocab = d2l.load_data_time_machine(batch_size, num_steps)
print(train_iter,vocab)