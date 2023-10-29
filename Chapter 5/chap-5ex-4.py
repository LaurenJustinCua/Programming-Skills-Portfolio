# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 20:00:16 2023

@author: Lauren Justin
"""

"""
Chapter 5 Excercise 4: Rivers
"""
rivers = {
    'Ural River': 'Russian',
    'Rhine River': 'Europe',
    'Congo River': 'Africa',
    'North Saskatchewan River': 'canada',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())