
import numpy as np

a = np.arange(15).reshape(3,5)
print("Dimension Coun = " +str(a.ndim))
print(a)
print(type(a))

b = np.arange(10)
print(b.shape)
print(b.ndim)