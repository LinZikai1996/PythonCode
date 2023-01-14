import pandas as pd
import numpy as np

stock_change = np.random.normal(0, 1, (10, 5))
print(stock_change)

stock_rise = pd.DataFrame(stock_change)
print(stock_rise)

print(stock_rise.shape)
print(stock_rise.shape[0])
print(stock_rise.shape[1])

stock_code = ["股票{}".format(i + 1) for i in range(stock_rise.shape[0])]
print(stock_code)

# 行索引
stock_rise = pd.DataFrame(stock_change, index=stock_code)
print(stock_rise)

# 列索引
# start 开始日期
# end 结束日期
# periods 时间跨度
# freq 统计时间方式
# freq 递进单位,默认为1,忽略周末'B'
date = pd.date_range(start="20190403", periods=stock_rise.shape[1], freq="B")
print(date)

stock_rise = pd.DataFrame(stock_change, index=stock_code, columns=date)
print(stock_rise)

# DataFrame
print(stock_rise.shape)
print(stock_rise.index)
print(stock_rise.columns)
print(stock_rise.values)
print(stock_rise.T)
print(stock_rise.head())
print(stock_rise.head(3))
print(stock_rise.tail())

# 重设索引
print(stock_rise.reset_index())
print(stock_rise.reset_index(drop=True))

df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2013, 2014, 2015],
                   'sale': [55, 44, 66, 33]})
print(df)
print(df.set_index(keys="year"))

# MultiIndex
df = df.set_index(keys=["year", "month"])
print(df)

print(df.index)
print(df.index.name)
print(df.index.levels)

# Series
print(type(stock_rise["2019-04-03"]))

print(pd.Series(np.arange(10)))
print(pd.Series([6.7, 5.6, 3, 10, 2], index=[1, 2, 3, 4, 5]))
