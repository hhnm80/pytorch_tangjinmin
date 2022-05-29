import torch
d = torch.randn(2,3)
print(d)

# 对d这个张量里面每个元素都加10
e = torch.add(d,10)
print(e)