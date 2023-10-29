# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:27:30 2023

@author: Lauren Justin
"""

"""
Chapter 3 Excercise 7:
"""
Guest = ['Lauren Cua', 'Abud Al Balooshi', 'Sedfrey Maulion', 'Paolo Signo']

print("Original order:")
print(Guest)

print("\nAlphabetical:")
print(sorted(Guest))

print("\nOriginal order:")
print(Guest)

print("\nReverse alphabetical:")
print(sorted(Guest, reverse=True))

print("\nOriginal order:")
print(Guest)

print("\nReversed:")
Guest.reverse()
print(Guest)

print("\nOriginal order:")
Guest.reverse()
print(Guest)

print("\nAlphabetical")
Guest.sort()
print(Guest)

print("\nReverse alphabetical")
Guest.sort(reverse=True)
print(Guest)