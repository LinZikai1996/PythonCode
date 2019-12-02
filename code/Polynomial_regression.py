import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


# load data
def load_data():
    return np.genfromtxt("../data/job.csv", delimiter=",")


def deal_with_data():
    data = load_data()
    data_x = data[1:, 1, np.newaxis]
    data_y = data[1:, 2, np.newaxis]
    return data_x, data_y


if __name__ == '__main__':
    data_x, data_y = deal_with_data()

    model = LinearRegression()
    model.fit(data_x, data_y)

    plt.plot(data_x, data_y, "b.")
    plt.plot(data_x, model.predict(data_x), "r")
    plt.show()

    # 进行特征处理
    polynomial_regression = PolynomialFeatures(degree=5)
    x = polynomial_regression.fit_transform(data_x)

    # 定义一个回归模型
    line_regression = LinearRegression()
    # 训练模型
    line_regression.fit(x, data_y)

    plt.plot(data_x, data_y, "b.")
    plt.plot(data_x, line_regression.predict(polynomial_regression.fit_transform(data_x)), c='r')
    plt.show()
