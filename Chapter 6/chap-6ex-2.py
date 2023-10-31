# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:40:18 2023

@author: Lauren Justin
"""

"""
Chapter 6 Excercise 2: Movie Ticket
"""
prompt = "HAII How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is AED 25.")
    else:
        print("  Your ticket is AED 35.")