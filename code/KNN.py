import numpy as np
import matplotlib.pyplot as plt

import Load_data
from Euclidean_distance import distance


def process_data():
    data = Load_data.load("moveType.csv")
    kind_type = data[:, -1]
    x = data[:, 0]
    y = data[:, 1]
    print(data)
    # kind_1_x = []
    # kind_1_y = []
    # kind_2_x = []
    # kind_2_y = []
    # for i in range(len(kind_type)):
    #     if kind_type[i] == 1:
    #         kind_1_x.append(x[i])
    #         kind_1_y.append(y[i])
    #     elif kind_type[i] == 2:
    #         kind_2_x.append(x[i])
    #         kind_2_y.append(y[i])
    # # 画图
    # plt.scatter(kind_1_x, kind_1_y, c='b', marker='o')
    # plt.scatter(kind_2_x, kind_2_x, c='r', marker='x')
    #
    # plt.show()
    data_x = data[:, :-1]
    data_y = data[:, -1]
    return data_x, data_y


if __name__ == '__main__':
    list_x, list_y = process_data()
    example = [150, 3]
    result_data = distance(list_x, example)
    type_class = {}

    for i in range(5):
        value = list_y[result_data[i]]
        type_class[value] = type_class.get(value, 0) + 1

    print(type_class)
