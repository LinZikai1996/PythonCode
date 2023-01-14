import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

movie = pd.read_csv("../data/IMDB-Movie-Data.csv")

average_score = movie["Rating"].mean()
print("电影平均分: " + str(round(average_score, 3)))

director_count = movie["Director"].unique().shape[0]
print("导演的个数: " + str(director_count))

print("电影平均分直方图")
movie["Rating"].plot(kind="hist")
plt.show()

print("电影平均分直方图 -version .1")
# 创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 绘制图像
plt.hist(movie["Rating"].values, 20)
# 显示 x 轴刻度
max_ = movie["Rating"].max()
min_ = movie["Rating"].min()
x1 = np.linspace(min_, max_, 21)
plt.xticks(x1)
plt.grid()
# 显示
plt.show()

print("电影分类")
print(movie["Genre"].head())

string_list = [i.split(",") for i in movie["Genre"]]
genre_list = np.unique([j for i in string_list for j in i])
print("电影分类" + str(genre_list))

genre_zero = pd.DataFrame(np.zeros((movie.shape[0], genre_list.shape[0])), columns=genre_list)
print(genre_zero)

for i in range(1000):
    genre_zero.loc[i, string_list[i]] = 1
print(genre_zero)

sum_list = genre_zero.sum().sort_values(ascending=False)
print(sum_list)

plt.figure(figsize=(20, 8), dpi=100)
# 绘制图像
plt.bar(genre_list, sum_list)
plt.show()
