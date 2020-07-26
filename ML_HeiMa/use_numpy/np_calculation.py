import numpy as np
import matplotlib.pyplot as plt

# 逻辑运算
stock_change = np.random.normal(0, 1, (8, 10))
print(stock_change)

stock_c = stock_change[0:5, 0:5]
print(stock_c)
print("-------------------------------------")

# 大于，小于直接判断
print(stock_c > 1)
print("-------------------------------------")

# 赋值：满足条件，直接赋值
stock_c[stock_c > 1] = 2
print(stock_c)
print("-------------------------------------")

# 通用判断函数
stock_d = stock_change[0:3, 0:3]
# 全部大于0，返回true
print(np.all(stock_d > 0))
print("-------------------------------------")
# 有一个大于0，返回true
print(np.any(stock_d > 0))
print("-------------------------------------")

# 三元运算符
# 满足条件，赋值第一个数值，否则第二个
print(np.where(stock_d > 0, 1, 0))
print("-------------------------------------")

# 逻辑与，逻辑或
print(np.where(np.logical_and(stock_d > -0.5, stock_d < 0.5), 1, 0))
print("-------------------------------------")

print(np.where(np.logical_or(stock_d > -0.5, stock_d < 0.5), 1, 0))
print("-------------------------------------")

# 最大值
# axis = 1 按照行进行统计
# # axis = 0 按照列进行统计
print(np.max(stock_c))

print(np.max(stock_c, axis=1))
print(np.max(stock_c, axis=0))
print("-------------------------------------")

# 返回最大值所在下标
# axis = 1 按照行进行统计
# # axis = 0 按照列进行统计
print(np.argmax(stock_c))
print(np.argmax(stock_c, axis=1))
print(np.argmax(stock_c, axis=0))

# 标准差
print(np.std(stock_c))

# 方差
print(np.var(stock_c))

# 中位数
print(np.median(stock_c))

# 平均值
print(np.mean(stock_c))

# 最小值
print(np.min(stock_c))

# 最小值下标
print(np.argmin(stock_c))