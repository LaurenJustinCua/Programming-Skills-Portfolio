# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:43:00 2023

@author: Lauren Justin
"""

"""
Chapter 6 Excercise 4: Delli
"""
sandwich_order = ['turkey sandwich', 'grilled cheese', 'bacon sandwich']
finished_sandwiches = []

while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print("Your Sandwich is on the way " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")