# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 20:40:02 2023

@author: Lauren Justin
"""

"""
Chapter 5 Excercise 5: Pet
"""
pets = []

pet = {
    'animal type': 'Cat',
    'name': 'Mingming',
    'owner': 'Lauren',
    'weight': 12,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'jose',
    'owner': 'Lauren',
    'weight': 55,
    'eats': 'dog food',
}
pets.append(pet)

pet = {
    'animal type': 'pig',
    'name': 'fatty',
    'owner': 'Lauren',
    'weight': 350,
    'eats': 'fruits',
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))