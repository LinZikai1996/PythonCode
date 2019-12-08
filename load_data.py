import numpy as np


def load(file_name, delimiter=","):
    return np.genfromtxt("../data/" + file_name, delimiter=delimiter)
