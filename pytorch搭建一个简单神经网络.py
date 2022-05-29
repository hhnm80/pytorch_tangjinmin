import torch
# batch_n 是在
# 一个批次中输入数据的数量，值是 100，这意味着我们在一个批次中输入 100 个数据，同
# 时，每个数据包含的数据特征有 input_data 个，因为 input_data 的值是 1000，所以每个数
# 据的数据特征就是 1000 个；
batch_n = 100
# hidden_layer 用于定义经过隐藏层后保留的数据特征的个数，
# 这里有 100 个，因为我们的模型只考虑一层隐藏层，所以在代码中仅定义了一个隐藏层的
# 参数；
hidden_layer = 100
input_data = 1000
output_data = 10

