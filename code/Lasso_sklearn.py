import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt

import Load_data


def process_data():
    data = Load_data.load("longley.csv")
    print(data)
    data_x = data[1:, 2:]
    data_y = data[1:, 1]
    return data_x, data_y


if __name__ == '__main__':
    data_x, data_y = process_data()
    model = linear_model.LassoCV()
    model.fit(data_x, data_y)

