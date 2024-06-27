from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import os
import torch

from torchvision.datasets import CIFAR100
class Cifar100Dataset(Dataset):
    def __init__(self, transforms=None, rootpath="./data"):
        self.trainset = CIFAR100(root=rootpath, download=False,train=True, transform=transforms)
        self.testset = CIFAR100(root=rootpath, download=False,train=False, transform=transforms)
        self.transform = transforms
    # def __getitem__(self, index):
    #     if torch.is_tensor(index):
    #         index = index.tolist()
    #     img_name = os.
        
    #     return super().__getitem__(index)
