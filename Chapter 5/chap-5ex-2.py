# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:50:25 2023

@author: Lauren Justin
"""

"""
Chapter 5 Excercise 2: Glossary
"""
glossary = {
    'string': 'a collection of alphabets, words or other characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'a data structure in Python that is a mutable, or changeable, ordered sequence of elements. ',
    'loop': 'repeating something over and over until a particular condition is satisfied.',
    'dictionary': "A collection of key-value pairs.",
    }
word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])