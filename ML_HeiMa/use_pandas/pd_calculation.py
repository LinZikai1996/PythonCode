import pandas as pd

data = pd.read_csv("../data/stock_day.csv")

# 直接使用方法, 也可以使用符号
print(data["close"].add(10))

# 逻辑运算
print(data[data["open"] > 23].head())

print(data[(data["open"] > 23) & (data["open"] < 24)].head())

print(data.query("open > 23 & open < 24").head())

print(data[data["open"].isin([23.53])])

# 统计运算
# 查看数据详细信息
print(data.describe())

print(data.sum())

# 累计统计函数
stock_rise = data["p_change"]
print(stock_rise.head())
stock_rise = stock_rise.cumsum()
print(stock_rise.head())

import matplotlib.pyplot as plt

stock_rise.plot()
plt.show()

# 自定义函数
print(data[['open']].apply(lambda x: x.max() - x.min(), axis=0))
