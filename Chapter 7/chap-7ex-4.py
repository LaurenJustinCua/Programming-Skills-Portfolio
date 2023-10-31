# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:05:50 2023

@author: Lauren Justin
"""

"""
Chapter 7 Excercise 4: Large Shirts
"""
def make_shirt(size='large', message='I love Python Soooo Much'):
    
    print("\nI'm going to make a " + size + " t-shirt.")
    print('Then it will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('large', 'Python The Best.')