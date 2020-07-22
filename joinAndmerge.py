# -*- coding: utf-8 -*-

import pandas as pd

data1 = {
         "id":[1,2,3],
         "isim":["alp","ali","erkan"],
         
         }
data2 = {
        "id":[1,2,3],
        "soyisim":["yenitürk","kaya","türk"],
        "durum":["evli","bekar","bekar"]
        }

data1Df = pd.DataFrame(data1)

data2Df = pd.DataFrame(data2)

print(data1)
print(data2)

print(pd.merge(data1Df,data2Df,on="id",how="inner"))
print(pd.merge(data1Df,data2Df,on="id",how="left"))
print(pd.merge(data1Df,data2Df,on="id",how="right"))

print(pd.concat([data1Df,data2Df],axis=1))