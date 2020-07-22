# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("positions.csv")
print(data.columns)

level = data.iloc[:,1].values.reshape(-1,1)
Salary = data.iloc[:,2].values.reshape(-1,1)
regression = DecisionTreeRegressor()
regression.fit(level,Salary)
print(regression.predict(8.51))


plt.scatter(level,Salary,color = "red")


x = np.arange(min(level),max(level),0.01).reshape(-1,1)
plt.plot(x,regression.predict(x),color = "green")
plt.xlabel("LEVEL")
plt.ylabel("SALARY")
plt.title("DECİONS TREE REGRESSION")
plt.show()