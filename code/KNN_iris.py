import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import operator
import random


def load_data():
    iris = datasets.load_iris()

    # 获取数据个数
    data_size = iris.data.shape[0]
    # 打乱数据集合
    random_index = random.shuffle([i for i in range(data_size)])
    iris.data = iris.data[random_index]
    iris.target = iris.target[random_index]

    # 切分数据集合
    text_data_size = 40
    train_x = iris.data[text_data_size:]
    train_y = iris.target[text_data_size:]
    test_x = iris.data[:text_data_size]
    test_y = iris.target[:text_data_size]

    # 使用内置函数,分割 0.2 为数据集合，0.8 为测试集合
    # train_data_x, train_data_y, test_data_x, test_data_y = train_test_split(iris.data, iris.target, test_size=0.2)
    return train_x, train_y, test_x, test_y


def KNN(train_x, train_y, test_x):
    x_size = train_x.shape[0]
    sort_list = np.array((((np.tile(test_x, (x_size, 1)) - train_x) ** 2).sum(axis=1) ** 0.5)).argsort()
    class_iris = {}
    for i in range(5):
        vote_label = train_y[sort_list[i]]
        class_iris[vote_label] = class_iris.get(vote_label, 0) + 1

    sort_result = sorted(class_iris.items(), key=operator.itemgetter(1), reverse=True)
    return sort_result[0][0]


if __name__ == '__main__':
    train_data_x, train_data_y, test_data_x, test_data_y = load_data()
    result = []
    for i in range(test_data_x.shape[0]):
        print("begin ..%d", i + 1)
        result.append(KNN(train_data_x, train_data_y, test_data_x[i]))

    print(result)
