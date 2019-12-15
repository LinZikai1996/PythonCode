import numpy as np


def distance(source_data, x_data):
    temp = np.tile(x_data, (source_data.shape[0], 1))
    result = ((temp - source_data) ** 2).sum(axis=1) ** 0.5
    return np.array(result).argsort()