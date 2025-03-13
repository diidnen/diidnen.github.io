import torch
from torch import nn
from d2l import torch as d2l

def vgg_block(num_convs,in_channels,out_channels):
    layers=[]
    for _ in range (num_convs):
        layers.append(nn.Conv2d(in_channels,out_channels,kernal_size=3,padding=1))
        layers.append(nn.ReLU())
        in_channels=out_channels
    layers.append(nn.MaxPool2d(kernel_size=2,stride=2))
    return nn.Sequential(*layers)


def vgg(conv_arch):
    conv_blks=[]
    in_channels=1
    for(num_convs,out_channels) in conv_arch




