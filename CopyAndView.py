# -*- coding: utf-8 -*-

import numpy as np
a = np.arange(10)
print(a)
b = a
print(b)

b[0] = 100
print(a)
print(b)

c = a.copy()
print(c)
c[0] = 120
print(a)
print(c)
c.shape = 2,5
print(c)
print(a)

d = a.view()
print(d)
d[0] = 350 
d.shape = 2,5
print(a)
print(d)