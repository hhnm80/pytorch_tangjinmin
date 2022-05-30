import torch

a=torch.IntTensor([1,2,9,-2,-1])
print(a.clamp(0))