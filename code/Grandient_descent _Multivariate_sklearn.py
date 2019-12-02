import numpy as np
import sklearn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 加载数据
def load_data():
    source_data = np.genfromtxt("../data/data.csv", delimiter=",")
    return source_data


if __name__ == '__main__':
    data = load_data()
    x_data = data[:, :-1]
    y_data = data[:, -1]

    model = sklearn.linear_model.LinearRegression()
    model.fit(x_data, y_data)
