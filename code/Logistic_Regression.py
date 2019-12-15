import numpy as np
import sklearn
import matplotlib.pyplot as plt
import Load_data

# 数据是否标准化
scale = False


def process_data(file_name):
    data = Load_data.load(file_name)
    print(data)
    data_x = data[:, :-1]
    data_y = data[:, -1, np.newaxis]
    return data_x, data_y


def picture(data_x, data_y):
    number = len(data_x)
    kind_1_parameter_1 = []
    kind_1_parameter_2 = []
    kind_2_parameter_1 = []
    kind_2_parameter_2 = []
    for i in range(number):
        if data_y[i] == 0:
            kind_1_parameter_1.append(data_x[i, 0])
            kind_1_parameter_2.append(data_x[i, 1])
        else:
            kind_2_parameter_1.append(data_x[i, 0])
            kind_2_parameter_2.append(data_x[i, 1])

    # 画图
    scatter_kind_1 = plt.scatter(kind_1_parameter_1, kind_1_parameter_2, c='b', marker='o')
    scatter_kind_2 = plt.scatter(kind_2_parameter_1, kind_2_parameter_2, c='r', marker='x')

    # 图例
    plt.legend(handles=[scatter_kind_1, scatter_kind_2], labels=['kind1', 'kind2'], loc='best')
    plt.show()


if __name__ == '__main__':
    data_x, data_y = process_data("LR-testSet.csv")
    data_x = np.concatenate((np.ones((100, 1)), data_x), axis=1)
    print(data_x.shape)
    picture(data_x, data_y)
