import torch

# 先生成第一个矩阵 并且赋值,在python里面,定义变量不用事先定义类型
# 从左往右 从外向里
a=torch.IntTensor([[1,2,3],[4,5,6]])

b=torch.IntTensor([[1,2],[3,4],[5,6]])

# 验证mm函数 就是a和b两个矩阵相乘 是标准的矩阵相乘,不是对应位元素相乘
c=a.mm(b)

# 输出tensor([[22, 28],
#         [49, 64]], dtype=torch.int32) 和手算结果一致
print(c)