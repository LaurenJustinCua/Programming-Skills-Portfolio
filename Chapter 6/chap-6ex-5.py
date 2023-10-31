# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:51:16 2023

@author: Lauren Justin
"""

"""
Chapter 6 Excercise 5: No pastrami
"""
sandwich_orders = [
    'pastrami', 'burger', 'grilled cheese', 'pastrami',
    'turkey sanwich', 'bacon sandwich', 'pastrami']
finished_sandwiches = []

print("We deeply apologize, we don't have pastrami at this time. ")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Your Sandwich is on the way " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")