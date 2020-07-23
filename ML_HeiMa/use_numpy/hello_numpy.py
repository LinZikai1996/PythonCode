import numpy as np

score = np.array([[10, 20, 30, 40, 50], [10, 20, 30, 40, 50], [10, 20, 30, 40, 50], [10, 20, 30, 40, 50]])

print(score)

# 看数组位数的元组
print(score.shape)

# 查看数组维数
print(score.ndim)

# 查看元素数量
print(score.size)

# 查看数组元素长度
print(score.itemsize)

# 查看元素类型
print(score.dtype)

# numpy Array的形状
a = np.array([1, 2, 3])

b = np.array([[1, 2, 3], [4, 5, 6]])

c = np.array([[[1, 2, 3], [1, 2, 3]], [[2, 3, 4], [2, 3, 4]]])

print(a)
print("-----")
print(b)
print("-----")
print(c)

print(c.shape)

