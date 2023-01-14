from sklearn.neighbors import KNeighborsClassifier

# data
x = [[1], [2], [0], [0]]
y = [1, 1, 0, 0]

# 实例化模型
estimator = KNeighborsClassifier(n_neighbors=2)
# 用fit方法训练
estimator.fit(x, y)
# 预测
print(estimator.predict([[1], [10], [-1], [0]]))
