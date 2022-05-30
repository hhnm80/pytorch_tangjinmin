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
#每个数据包含的数据特征有 input_data 个，因为 input_data 的值是 1000，所以每个数
# 据的数据特征就是 1000 个；
input_data = 1000

# output_data 是输出的数据，值是 10，我们可以将输出的数据看作一个分类结果值的数量，个数 10 表示我们最后要得到 10 个分类结果值。
output_data = 10
# 一个批次的数据从输入到输出的完整过程是：先输入 100 个具有 1000 个特征的数据，
# 经过隐藏层后变成 100 个具有 100 个特征的数据，再经过输出层后输出 100 个具有 10 个
# 分类结果值的数据，在得到输出结果之后计算损失并进行后向传播，这样一次模型的训练
# 就完成了，然后循环这个流程就可以完成指定次数的训练，并达到优化模型参数的目的。下
# 面看看如何完成从输入层到隐藏层、从隐藏层到输出层的权重初始化定义工作，代码如下：
a=torch.randn(4)
# 为什么会有负数呢?????为什么张量里面会有负数呢?????难道这里面是x的值的分布么????
print(a)

# 在第一次执行下面代码的时候，batch_n值为100,input_data值是1000,根据这两个参数,构成了张量的形状.就是一个二维数组,100行,1000列的二维张量,或者简单说是二维数组
x = torch.randn(batch_n, input_data)
# 100行 10列的二维张量,或者说是二维数组
y = torch.randn(batch_n, output_data)
# 1000行，100列张量
w1 = torch.randn(input_data, hidden_layer)
# 100行，10列张量
w2 = torch.randn(hidden_layer, output_data)
#张量的形状与后面的矩阵运算有很大关系,按照二维矩阵的乘积运算规则,两个矩阵相乘,第一个矩阵的列数必须与第二个矩阵的行数相同,

# 在定义好输入、输出和权重参数之后，就可以开始训练模型和优化权重参数了，在此
# 之前，我们还需要明确训练的总次数和学习速率，代码如下：
# 训练总次数  训练20次????
epoch_n = 20
# 学习速率 1e-6表示1乘以10的负6次方。e-6不是e的-6次方,是10的-6次方,一个指数形式函数包括两部分,一部分是常数部分,比如这里的1,1*10^-6
learning_rate = 1e-6

# 由于上面定义epoch_n的值为20,训练次数是20次,因此我们需要写一个循环体,执行20次,,,,,来完成对初始化权重参数的优化和调整,,,,接下来对模型进行正式训练并对参数进行优化，代码如下：
# 因为epoch_n的值为20,range(20)得到一个列表,有20个元素,即[0,1,2,3..........19],迭代到epoch里面的值就是0,1,2,3......这似乎是一个列表或者数组的索引:
for epoch in range(epoch_n):
    #100*1000  mm函数是pytorch里面的一个函数,这个函数的作用可以百度得知>>>>在这里mm函数只有一个参数,只有一个参数,只有一个参数,只有一个参数,这一个参数有什么意义呢????其实下面这个语句的含义就是x这个矩阵和w1这个矩阵相乘,x的shape是100*1000,而w1的shape是1000*100,所以x和w1这两个矩阵可以相乘,得到h1是一个100*100的矩阵

    #得到 100*100
    h1=x.mm(w1)
    # clamp函数,百度查看这个函数的定义,,这个函数只有一个参数,假设有一个a=torch.IntTensor([1,2,9,-2,-1])这样的张量,则a.clamp(0)后得到的张量是tensor([1, 2, 9, 0, 0], dtype=torch.int32)....这说明,原来张量里面小于0的值变成了0,,这和relu激活函数的功能几乎一致....
    h1=h1.clamp(min=0)
    # 这又是什么呢,让h1,就是被处理后的矩阵,这时候h1这个矩阵里面所有的元素都是非负,,,h1和w2相乘得到什么呢???结果是一个100行10列的矩阵,
    y_pred = h1.mm(w2)  #得到 100*10

    # 这里面给定了一个y值 y是一个100行 10列的张量,y_pred也是一个100行10列的张量,这里要知道y_pred矩阵的来源,为了方便理解,下面所有的张量我们都以矩阵代替,
    loss=(y_pred-y).pow(2).sum();
