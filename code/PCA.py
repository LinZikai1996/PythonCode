import numpy as np
import matplotlib.pyplot as plt
import Load_data


def process_data(data):
    data_x = data[:, 0]
    data_y = data[:, 1]
    return data_x, data_y


def show_data(name, x):
    print("-----------" + name + "-----------")
    print(x.shape)
    print(x)


# 数据中心化
def zero_mean(source_data):
    # 每一列的平均值
    mean = np.mean(source_data, axis=0)
    new = source_data - mean
    return new, mean


# data的协方差矩阵
def covariance(new):
    # np.cov用于求协方差矩阵，参数rowvar表示一行代表一个样本
    cov = np.cov(new, rowvar=0)
    return cov


# 获取特征值和特征向量
def eigenvalue_and_eigenvector(cov):
    eigenvalue, eigenvector = np.linalg.eig(np.mat(cov))
    return eigenvalue, eigenvector


if __name__ == '__main__':
    data = Load_data.load("data.csv")
    show_data("data", data)
    new_data, mean_value = zero_mean(data)
    show_data("new_data", new_data)
    show_data("mean_value", mean_value)
    cov_data = covariance(new_data)
    show_data("cov_data", cov_data)
    eigenvalue_data, eigenvector_data = eigenvalue_and_eigenvector(cov_data)
    show_data("eigenvalue_data", eigenvalue_data)
    show_data("eigenvector_data", eigenvector_data)
    # 从小到大排序
    eigenvalue_Index_data = np.argsort(eigenvalue_data)
    show_data("eigenvalue_Index_data", eigenvalue_Index_data)
    top = 1
    # 最大的top个下标
    n_eigenvalue_Index_data = eigenvalue_Index_data[-1:-(top + 1):-1]
    show_data("n_eigenvalue_Index_data", n_eigenvalue_Index_data)
    n_eigenvector_data = eigenvector_data[:, n_eigenvalue_Index_data]
    show_data("n_eigenvector_data", n_eigenvector_data)
    low_data = new_data * n_eigenvector_data
    show_data("low_data", low_data)

    # 利用低维数据从构造数据
    re_data = (low_data * n_eigenvector_data.T) + mean_value
    show_data("re_data", re_data)
    old_x, old_y = process_data(data)
    new_x, new_y = process_data(np.array(re_data))
    plt.scatter(old_x, old_y, c="b")
    plt.scatter(new_x, new_y, c="r")
    plt.show()
