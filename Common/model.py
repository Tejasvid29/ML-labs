import torch.nn as nn
from torchvision.models import resnet18

def get_model(num_classes = 10):
    #Returns a ResNet-18 model adapted for CIFAR-10.
    model = resnet18(weights = None)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model


#Defines the structure of the output data