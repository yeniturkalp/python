# -*- coding: utf-8 -*-

import pandas as pd
url = "http://bit.ly/uforeports"

data = pd.read_csv(url)
print(data)
print(data.isnull().head())
print(data[data.City.isnull()])
print(data.isnull().sum())

print(data.shape)
#data = data.dropna(how = "any")
#data = data.dropna(subset = ['City','Colors Reported'],how = "all")

data['Shape Reported'].fillna(value='Belirsiz',inplace =True)
print(data['Shape Reported'].value_counts(dropna=False))



print(data.shape)
