import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("../data/data.csv", delimiter=",")

data_x = data[:, 0, np.newaxis]
data_y = data[:, 1, np.newaxis]

plt.scatter(data_x, data_y)
plt.show()

print(np.mat(data_x))
