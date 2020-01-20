"""
Working with Build-In

Build In -> Module inside of the Python

# Using alias to funciton
import random as rdm

print(rdm.random())


# import all functions
from random import *
# do not need the name random.random()
print(random())

print(random())

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())
"""

from random import (
    random,
    randint,
    shuffle,
    choice
)
print(randint(5, 89))
print(random())
print(choice('Yumi Ouchi'))
list_number = ['Geek', 'Yumi']
shuffle(list_number)
print(list_number)
