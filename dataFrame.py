# -*- coding: utf-8 -*-

import pandas as pd
data = [1,23,4,5]
df = pd.DataFrame(data)
print(df)

#data2 = [["alp",23,"bayburt"],["veli",25,"ankara"],["ali",21,"bursa"]
#df2 = pd.DataFrame(data2,columns=["isim","yaş","şehir"],index=[1,2,3])






data3 = {"isim":["alp","veli","ali"],
         "yaş":[23,25,21],
         "şehir":["bayburt","ankara","bursa"]}
df3 = pd.DataFrame(data3)
print(df3)
#df3.pop("şehir")
#del df3("şehir")