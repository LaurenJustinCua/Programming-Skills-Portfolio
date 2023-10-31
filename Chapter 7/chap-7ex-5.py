# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:08:06 2023

@author: Lauren Justin
"""

"""
Chapter 7 Excercise 5: Cities
"""
def describe_city(city, country='UAE'):
    
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Dubai')
describe_city('Abu Dhabi', 'UAE')
describe_city('Ras Al Khaimah')