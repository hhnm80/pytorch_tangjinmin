import torch
import numpy

a=torch.IntTensor([1,2,9,-2,-1])
# 输出tensor([ 1,  4, 81,  4,  1], dtype=torch.int32) 看来pow函数是对矩阵的每个元素进行乘方操作,在这里是2次方,也就对矩阵里面每个元素进行平方操作,是矩阵元素的乘方,不是矩阵的乘方,因为矩阵的乘方必须符合矩阵的乘方的法则,就是链式法则.第一个的列数必须等于第二个矩阵的行数....才能够相乘,才能够衔接.....
print(a.pow(2))
# 输出91
print(a.pow(2).sum())

a=torch.IntTensor([[1,2],[3,4]])

# 输出tensor([[1, 3],
#         [2, 4]], dtype=torch.int32)
print(a.t())

c=a.clone();
print(a)
print(c)



