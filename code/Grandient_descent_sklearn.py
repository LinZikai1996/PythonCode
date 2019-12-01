from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


# 加载数据
def load_data():
    source_data = np.genfromtxt("../data/data.csv", delimiter=",")
    return source_data


if __name__ == '__main__':
    data = load_data()

    # fit()函数要求数据多一维
    data_x = data[:, 0, np.newaxis]
    data_y = data[:, 1, np.newaxis]
    # 创建模型，并且拟合模型
    model = LinearRegression()
    model.fit(data_x, data_y)

    # 画图
    plt.plot(data_x, data_y, "b.")
    plt.plot(data_x, model.predict(data_x), "r")
    plt.show()
