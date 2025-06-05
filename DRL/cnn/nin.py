import torch
from torch import nn
from d2l import torch as d2l

def nin_block(in_channels, out_channels, kernel_size, strides, padding):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, kernel_size, strides, padding), nn.ReLU(),
        nn.Conv2d(out_channels, out_channels, kernel_size=1), nn.ReLU(),
        nn.Conv2d(out_channels, out_channels, kernel_size=1), nn.ReLU(),
    )


net = nn.Sequential(
    nin_block(1, 96, 11, 4, 0),
    nn.MaxPool2d(kernel_size=3, stride=2),
    nin_block(96, 256, 5, 1, 1),
    nn.MaxPool2d(kernel_size=3, stride=2),
    nin_block(256, 384, 3, 1, 1),
    nn.MaxPool2d(kernel_size=3, stride=2),
    nn.Dropout(0.5),
    nin_block(384, 10, 3, 1, 1),
    nn.AdaptiveAvgPool2d((1,1)),
    nn.Flatten()
)

X  = torch.randn(size=(1,1,224,224))
for layer in net:
    X = layer(X)
    print(layer.__class__.__name__, 'output shape: ', X.shape)

lr, num_epochs, batch_size = 0.1, 10, 128
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size, resize=224)
d2l.train_ch6(net, train_iter, test_iter, num_epochs, lr, d2l.try_gpu())