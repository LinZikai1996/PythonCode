import numpy as np
import matplotlib.pyplot as plt


# 加载数据
def load_data():
    source_data = np.genfromtxt("../data/data.csv", delimiter=",")
    return source_data


# 代价函数，使用最小二乘法
def cost_function(k, b, data_x, data_y):
    total_error = 0
    for i in range(0, len(data_x)):
        total_error += (data_y[i] - (k * data_x[i] + b)) ** 2
    return total_error / float(len(data_x)) / 2.0


# 一元梯度下降法
def gradient_descent_function(data_x, data_y, k, b, learning_rate, max_number_of_iterations):
    # 数据的总量
    number = float(len(data_x))
    for i in range(max_number_of_iterations):
        temp_b = 0
        temp_k = 0
        for j in range(len(data_x)):
            temp_b += (1 / number) * (data_x[j] * k + b - data_y[j])
            temp_k += (1 / number) * (data_x[j] * k + b - data_y[j]) * data_x[j]

        b = b - (learning_rate * temp_b)
        k = k - (learning_rate * temp_k)

        if i % 5 == 0:
            print("max_number_of_iterations",i)
            plt.plot(data_x, data_y, "b.")
            plt.plot(data_x, k * data_x + b, "r")
            plt.show()

    return k, b


if __name__ == '__main__':
    source_data = load_data()
    # 表示获取数据的所有行的第零列
    data_x = source_data[:, 0]
    # 表示获取数据的所有行的第一列
    data_y = source_data[:, 1]
    # 学习率
    learning_rate = 0.0001
    # 初始截距
    b = 0
    # 初始斜率
    k = 0
    # 最大迭代次数
    max_number_of_iterations = 50

    print("Starting b = {0}, k = {1} , error = {2}".format(b, k,
                                                           cost_function(k, b, data_x, data_y)))
    print("Running ...")
    k, b = gradient_descent_function(data_x, data_y, k, b, learning_rate, max_number_of_iterations)

    print("Starting b = {0}, k = {1} , error = {2}".format(b, k,
                                                           cost_function(k, b, data_x, data_y)))

    # plt.plot(data_x, data_y, "b.")
    # plt.plot(data_x, k * data_x + b, "r")
    # plt.show()
