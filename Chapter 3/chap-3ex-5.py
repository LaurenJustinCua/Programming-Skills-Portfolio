# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:17:56 2023

@author: Lauren Justin
"""

"""
Chapter 3 Excercise 4:
"""
guests = ['Sedfrey Maulion', 'Abud Al balooshi', 'Lauren Cua']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[1])
guests.insert(1, 'Paolo Signo')

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")