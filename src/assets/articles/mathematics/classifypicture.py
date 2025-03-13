import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l
import matplotlib.pyplot as plt

d2l.use_svg_display()
trans=transforms.ToTensor()
mnist_train=torchvision.datasets.FashionMNIST(
    root="../data",
    train=True,
    transform=trans,
    download=True
)

mnist_test = torchvision.datasets.FashionMNIST(
    root="../data", train=False, transform=trans, download=True)

print(len(mnist_test),len(mnist_train))

mnist_train[0][0].shape

def get_fashion_mnist_labels(labels):
    text_labels=['t-shirt','trouser','pullover','pullover','dress','coat','sandal','shirt','sneaker','bag','ankle boot']
    return [text_labels[int(i)] for i in labels]

def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):  #@save
    """绘制图像列表"""
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):
            # 图片张量
            ax.imshow(img.numpy())
        else:
            # PIL图片
            ax.imshow(img)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    plt.show()
    return axes

X,y=next(iter(data.DataLoader(mnist_train,batch_size=18)))
show_images(X.reshape(18,28,28),2,9,titles=get_fashion_mnist_labels(y))

batch_size =256
def get_dataloader_workers():
    return 4

train_iter=data.Dataloader(mnist_train,batch_size,shuffle=True,num_workers=get_dataloader_worders)

timer=d2l.Timer()
for X,y in train_iter:
    continue
print(f'{timer.stop():.2f} sec')

def load_data_fashion_mnist(batch_size,resize=None):
    trans=[transforms.ToTensor()]
    if resize:
        trans.insert(0,transforms.Resize(resize))
    trans=transforms.Compose(trans)
    return (data.DataLoader(mnist_train, batch_size,shuffle=True,num_workers=get_dataloader_workers()),
            data.DataLoader(mnist_test, batch_size,shuffle=True,num_workers=get_dataloader_workers()))



