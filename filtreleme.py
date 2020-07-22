# -*- coding: utf-8 -*-

import pandas as pd

films = pd.read_csv("imdb-1000.csv")
print(films)
print(films.columns)
print(films.tail())
print(films.head())

print(films.title.head)
print(films[:9][["title","star_rating","actors_list"]])
print(films[(films["star_rating"]>=8.2)&(films["star_rating"]>=9)][["title","star_rating","actors_list"]])
print(films[(films["star_rating"]>=8.2)&(films["star_rating"]>=9)][["title","star_rating"]])

print(films.query('star_rating >=9 & star_rating <= 9.3')[["title","star_rating"]])