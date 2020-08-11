import pandas as pd

data = pd.read_csv("../data/stock_day.csv")

# 直接使用方法, 也可以使用符号
print(data["close"].add(10))

# 逻辑运算
print(data[data["open"] > 23].head())

print(data[(data["open"] > 23) & (data["open"] < 24)].head())

print(data.query("open > 23 & open < 24").head())

print(data[data["open"].isin([23.53])])
