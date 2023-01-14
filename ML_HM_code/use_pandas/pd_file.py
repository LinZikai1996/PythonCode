import pandas as pd

# csv文件
data = pd.read_csv("../data/stock_day.csv", usecols=["open", "high"])
print(data)

data[:10].to_csv("../data/test_to_csv.csv", columns=["open"], index=True)

# hdf文件
# 推荐
h5_data = pd.read_hdf("../data/day_employee.h5")
print(h5_data)

h5_data[:].to_hdf("../data/test_to_hdf.h5", key="close")

# json文件
# orient 按照什么方式读取
json_data = pd.read_json("../data/Sarcasm_Headlines_Dataset.json", orient="records", lines=True)
print(json_data)

json_data.to_json("../data/test_to_json.json", orient="records", lines=True)
