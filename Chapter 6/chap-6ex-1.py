# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:37:49 2023

@author: Lauren Justin
"""

"""
Chapter 6 Excercise 1: Pizza Toppings
"""
prompt = "\nHello, What topping would you like on your pizza?"
prompt += "\nPlease Enter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I will add " + topping + " to your pizza.")
    else:
        break