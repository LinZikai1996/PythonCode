import pandas as pd

stock_data = pd.read_csv("../data/stock_day.csv")

print(stock_data.head())
stock_data = stock_data.drop(["ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"], axis=1)
print(stock_data)

# pandas 索引, 先列后行, 不可以先行后列
print(stock_data["open"]["2018-02-27"])

# 先行后列
print(stock_data.loc["2018-02-27":"2018-02-23", "high"])

print(stock_data.iloc[:3, :5])

# 排序, ascending=True升序, ascending=False降序
print(stock_data.sort_values(by="open", ascending=True).head())

print(stock_data.sort_values(by=['open', 'high']))

print(stock_data.sort_index())

# series
print(stock_data["open"].sort_values(ascending=False).head())
