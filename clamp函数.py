import torch

a=torch.IntTensor([1,2,9,-2,-1])


# print(a.clamp(min=0));

print(a.clamp_(0))