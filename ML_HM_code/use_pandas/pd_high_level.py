import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 缺失值处理
wis = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
print(wis)

wis = wis.replace(to_replace="?", value=np.NaN)

print(np.any(pd.isnull(wis)))
print(np.any(pd.isnull(wis.dropna())))

# 离散化处理
data = pd.read_csv("../data/stock_day.csv")
print(data.head())

data_p = data["p_change"]

# 自动分组
data_qcut = pd.qcut(data_p, q=10)
print(data_qcut)
# 统计分组次数
print(data_qcut.value_counts())

# 自定义分组
bins = [-100, -7, -5, -3, 0, 3, 5, 7, 100]
data_cut = pd.cut(data_p, bins)
print(data_cut)
# 统计分组次数
print(data_cut.value_counts())

print(pd.get_dummies(data_cut, prefix="class"))

# 数据合并
# pd.concat()
# pd.merge()

# 交叉表和透视表
print(data.index)
time = pd.to_datetime(data.index)

print(time.day)
print(time.week)
print(time.weekday)

data["week"] = time.weekday
print(data.head())

data["p_n"] = np.where(data["p_change"] > 0, 1, 0)
print(data.head())

count = pd.crosstab(data["week"], data["p_n"])
print(count)

data_sum = count.sum(axis=1)
print(data_sum)
data_per = count.div(data_sum, axis=0)
print(data_per)

data_per.plot(kind="bar", stacked=True)
plt.show()

print(data.pivot_table(["p_n"], index="week"))

# 分组聚合
col = pd.DataFrame(
    {'color': ['white', 'red', 'green', 'red', 'green'], 'object': ['pen', 'pencil', 'pencil', 'ashtray', 'pen'],
     'price1': [5.56, 4.20, 1.30, 0.56, 2.75], 'price2': [4.75, 4.12, 1.60, 0.75, 3.15]})

col.groupby(['color'])['price1'].mean()

col['price1'].groupby(col['color']).mean()