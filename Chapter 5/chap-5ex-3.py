# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:54:45 2023

@author: Lauren Justin
"""

"""
Chapter 5 Excercise 2: 
"""
glossary = {
    'string': 'a collection of alphabets, words or other characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'a data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
    'loop': 'repeating something over and over until a particular condition is satisfied.',
    'dictionary': "a collection of key-value pairs",
    'key': 'analogous to indexes of a list.',
    'value': 'one of the basic things a program works with, like a letter or a number',
    'conditional test': 'fundamental programming constructs that allow you to control the flow of your program based on conditions that you specify.',
    'float': 'a function or reusable code in the Python programming language that converts values into floating point numbers.',
    'boolean expression': 'an expression that evaluates to produce a result which is a Boolean value.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
    