import numpy as np
import matplotlib.pyplot as plt

# 返回[0.0, 1.0]之间的一组均匀分布的数
a1 = np.random.rand(2, 3)
print(a1)
print("----------------------------------")

# 从[low, high]随机采样，定义域包含low,不包含high
a2 = np.random.uniform(low=0, high=10, size=(3, 6))
print(a2)
print("----------------------------------")

# 生成整数的均匀分布
a3 = np.random.randint(1, 10, (3, 5))
print(a3)
print("----------------------------------")

# e.g
# 生成均匀分布的随机数
x1 = np.random.uniform(0, 1, 10000000)

plt.figure(figsize=(10, 8), dpi=100)

plt.hist(x=x1, bins=1000)

plt.show()
print("----------------------------------")

# 生成正态分布
# API: (均值，方差，个数)
x2 = np.random.normal(1.75, 1, 1000000)

plt.figure(figsize=(10, 8), dpi=100)

plt.hist(x=x2, bins=1000)

plt.show()
print("----------------------------------")

# e.g
stock_change = np.random.normal(0, 1, (4, 5))
print(stock_change)

# 数据索引和切片
# 拿到前两行，前三列，先对行进行索引
print(stock_change[0:2, 0:3])

# 形状修改
# reshape 和 resize 没有进行转置，只是重新排列
# reshape产生新列，resize对原来进行更改
print(stock_change.reshape([5, 4]))
# 使用T进行转置
print(stock_change.T)

# 修改类型
print(stock_change.astype(np.int))

# 数组去重
a4 = np.array([[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7]])
print(np.unique(a4))
