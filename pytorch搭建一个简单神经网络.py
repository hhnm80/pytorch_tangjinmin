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

print("y值是:",y)
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

    #得到 100*100矩阵
    # 输出x和w1的值
    print("x值是:", x)
    print("w1值是:", w1)

    h1=x.mm(w1)
    # clamp函数,百度查看这个函数的定义,,这个函数只有一个参数,假设有一个a=torch.IntTensor([1,2,9,-2,-1])这样的张量,则a.clamp(0)后得到的张量是tensor([1, 2, 9, 0, 0], dtype=torch.int32)....这说明,原来张量里面小于0的值变成了0,,这和relu激活函数的功能几乎一致....
    h1=h1.clamp(min=0)
    # 这又是什么呢,让h1,就是被处理后的矩阵,这时候h1这个矩阵里面所有的元素都是非负,,,h1和w2相乘得到什么呢???结果是一个100行10列的矩阵,
    # y_pred是一个100*10的矩阵
    y_pred = h1.mm(w2)  #得到 100*10

    # 这里面给定了一个y值 y是一个100行 10列的张量,y_pred也是一个100行10列的张量,这里要知道y_pred矩阵的来源,为了方便理解,下面所有的张量我们都以矩阵代替,y_pred的来源是
    # x与w1相乘,然后将得到的矩阵里面的负数全部变为0,然后再与w2矩阵相乘,就是说三个相乘里面多了一步化负为0,当然上面矩阵里面的非负数,就不变了
    # 因为y_pred-y还是一个矩阵,对矩阵元素进行平方以后,然后就是对矩阵里面每个元素相加,假设y_pred-y是[1,2],执行pow(2)操作后得到[1,4],执行sum操作后得到5,最后loss是一个数值,我们用这个数值来衡量损失率么??????????
    loss=(y_pred-y).pow(2).sum();
    #输出Epoch:0, Loss:41555568.0000
    # Epoch:1, Loss:41555568.0000
    # 这是怎么输出的呢?????还是用字符串填坑,坑是什么呢???就是这里面的大括号,epoch填入第一个大括号,但是是原模原样的填进去,format  .4f就是保留4位小数,没有小数就补0

    # 根据打印信息，我们关注的便是loss值的变化，那么我们要不要把每次预测的值和真实值打印出来呢？？？这样不就更能体现神经网络在训练的时候数据的变化么,epoch的值从0开始,这里代表第epoch+1次循环,第一次循环的时候,此时loss是多少呢???每次输出loss之前,要先算loss的值,按照上面式子,loss由y_pred和y决定,但是程序运行一次,y只赋值一次,因此loss由y_pred决定,而且由于x也是不变的,变与不变,我们看循环体里面有没有对变量进行赋值操作就可以了????
    print("Epoch:{}, Loss:{:.4f}".format(epoch, loss))

    # 给grad_y_pred这个变量赋值 两个矩阵相减,然后把里面每个元素扩大二倍,,,,
    # 矩阵
    # 100*10
    grad_y_pred = 2 * (y_pred - y)
    # torch的mm函数是矩阵相乘,对h1这个矩阵转置以后,得到一个100*100矩阵,然后这个矩阵与grad_y_pred矩阵相乘,grad_y_pred是100*10矩阵,    最后grad_w2是100*10矩阵 grad在英文里面是"梯度"的意思
    # 100*10矩阵
    grad_w2 = h1.t().mm(grad_y_pred)
    #对grad_y_pred克隆,那么grad_h这个矩阵和grad_y_pred一模一样
    grad_h = grad_y_pred.clone()

    # grad_h与w2的转置矩阵相乘,grad_h是100*10  w2是100*10 w2的转置是10*100 因此grad_h是100*100
    # 100*100
    grad_h = grad_h.mm(w2.t())
    print(grad_h.shape)

    # 上面已经学习了clamp函数,那么clamp_函数又是什么呢?????和clamp函数一样,由于这里定义的形参是min=0,或者说实参,其实是实参,实参叫min,作为clamp_函数的一个参数传入,就像占座位一样,值为0,就是将grad_h矩阵里面的负数元素变成0,
    grad_h.clamp_(min=0)
    # 对x矩阵转置然后与grad_h相乘
    grad_w1 = x.t().mm(grad_h)

    # w1-=就是对w1重新赋值,什么重新赋值呢,就是循环没执行一次,w1的值减少learning_rate * grad_w1,但是grad_w1是一个变量,每次循环grad_w1的值不一样,因此每次循环执行到这里,w1减少的值不一样......
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2


# 运行程序输出：Epoch:0, Loss:63756024.0000
# torch.Size([100, 100])
# Epoch:1, Loss:199783216.0000
# torch.Size([100, 100])
# Epoch:2, Loss:768902400.0000
# torch.Size([100, 100])
# Epoch:3, Loss:540055552.0000
# torch.Size([100, 100])
# Epoch:4, Loss:6571139.0000
# torch.Size([100, 100])
# Epoch:5, Loss:5095245.0000
# torch.Size([100, 100])
# Epoch:6, Loss:4074880.2500
# torch.Size([100, 100])
# Epoch:7, Loss:3339844.0000
# torch.Size([100, 100])
# Epoch:8, Loss:2793061.0000
# torch.Size([100, 100])
# Epoch:9, Loss:2376278.7500
# torch.Size([100, 100])
# Epoch:10, Loss:2052290.3750
# torch.Size([100, 100])
# Epoch:11, Loss:1795993.8750
# torch.Size([100, 100])
# Epoch:12, Loss:1589838.8750
# torch.Size([100, 100])
# Epoch:13, Loss:1421996.0000
# torch.Size([100, 100])
# Epoch:14, Loss:1283567.7500
# torch.Size([100, 100])
# Epoch:15, Loss:1168031.5000
# torch.Size([100, 100])
# Epoch:16, Loss:1070657.3750
# torch.Size([100, 100])
# Epoch:17, Loss:987706.2500
# torch.Size([100, 100])
# Epoch:18, Loss:916323.5625
# torch.Size([100, 100])
# Epoch:19, Loss:854287.2500
# torch.Size([100, 100])


