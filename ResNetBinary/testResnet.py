import os
import numpy as np
from PIL import Image
from torch.utils import data
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import torchvision.transforms as transforms
from tqdm import tqdm


if __name__ == "__main__":
    
    resnet = models.resnet18(pretrained=True)
    modules = list(resnet.children())[:-4]      # delete the last fc layer.
    avgpool = nn.AdaptiveMaxPool2d((1,1))
    modules.append(avgpool)
    resnet = nn.Sequential(*modules)
    
    x = torch.randn(2,3,64,64)
    
    
    xx = resnet(x)
    
    print("hello")
    