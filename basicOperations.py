# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1,5,7,8])
b = np.arange(4)

c = a-b
print(b**2)

print(a*b)
print(a@b)
print(a.dot(b))
d = np.zeros((2,4))
e = np.ones((2,4))
k = np.sqrt(b)
t = np.min(b)
x = np.random.random((2,4))
i = np.max(x)