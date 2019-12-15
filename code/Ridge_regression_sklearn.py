import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt

# load data
import Load_data


def process_data():
    data = Load_data.load("longley.csv")
    print(data)
    data_x = data[1:, 2:]
    data_y = data[1:, 1]
    return data_x, data_y


if __name__ == '__main__':
    data_x, data_y = process_data()
    # 创建模型
    # 生成50个值
    alphas_to_test = np.linspace(0.001, 1, 1000)
    # 创建模型
    model = linear_model.RidgeCV(alphas=alphas_to_test, store_cv_values=True)
    model.fit(data_x, data_y)

    # 岭系数
    print(model.alpha_)
    # loss值
    print(model.cv_values_.shape)

    # 画图
    plt.plot(alphas_to_test, model.cv_values_.mean(axis=0))
    plt.plot(model.alpha_, min(model.cv_values_.mean(axis=0)), 'ro')
    plt.show()
