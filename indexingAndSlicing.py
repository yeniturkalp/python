# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")

notlar.columns = ["isim","soyisim","SSN","test1","test2","test3",
                  "test4","final","sonuç"]

print(notlar)

print(notlar.loc[:5,"isim":"final"])
print(notlar.loc[::-1,"isim"])
print(notlar.loc[:5,["isim","soyisim","final"]])