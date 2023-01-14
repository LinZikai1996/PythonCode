import numpy as np

# 生成数组,全1
ones = np.ones([4, 8])
print(ones)

# 生成全0数组
zeros = np.zeros_like(ones)
print(zeros)

# 生成索引
a = np.array([[1, 2, 3], [1, 2, 3]])
a1 = np.array(a)
print(a1)

a2 = np.asarray(a)
print(a2)

a[0, 0] = 100
print(a)
print(a1)
print(a2)

# 生成序列
# linspace(start, stop, num, endpoint)
b = np.linspace(0, 100, 11)
print(b)

# arange(start, stop, step, dtype)
c = np.arange(10, 50, 2)

# logspace(start, stop, num)
# 10^x
d = np.logspace(0, 2, 3)
