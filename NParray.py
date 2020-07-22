# -*- coding: utf-8 -*-

import numpy as np
a = np.array([1,5,7,3,8,9])
a = a.reshape(2,3)
print(a.dtype)
print(a.ndim)
print(a)
print("********")

b = np.array([[1,5],[7,3],[8,9]])
print(b)
print(b.ndim)