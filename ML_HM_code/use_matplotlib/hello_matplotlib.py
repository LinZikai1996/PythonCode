import matplotlib.pyplot as plt

# 1.create plan

plt.figure(figsize=(20, 8), dpi=100)

# 2.draw pic
x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)

# 3.show pic
plt.show()

# 4.save pic
plt.savefig("./data/Test.png")
