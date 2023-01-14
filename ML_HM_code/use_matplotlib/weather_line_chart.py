import random

import matplotlib.pyplot as plt

# 生成数据
x = range(60)

y = [random.uniform(10, 15) for i in x]

# print(y)

# 创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 绘制图像
plt.plot(x, y, label="beijing")

# 添加x, y刻度
y_ticks = range(40)
# 刻度为0 - 40, 每个格子表示 5
plt.yticks(y_ticks[::5])

x_ticks_labels = [" 11:{}:00".format(i) for i in x]

plt.xticks(x[::5], x_ticks_labels[::5])

# 添加网格
plt.grid(True, linestyle="--", alpha=0.5)

# 添加描述
plt.xlabel("time")
plt.ylabel("value")
plt.title("title", fontsize=20)

# 显示图例

plt.legend(loc="best")

# 图像展示

plt.show()
