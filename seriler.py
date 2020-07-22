# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 01:28:18 2019

@author: asus
"""

import pandas as pd
import numpy as np

data = np.array(["alp","ali","veli"])

s = pd.Series(data , index=[1,2,3])
print(s)

data2 = {"mat":10,"fiz":15,"kim":55}
s2 = pd.Series(data2,index=["fiz","kim","mat"])
print(s2)

s3 = pd.Series(5,index=[1,2])
print(s3)