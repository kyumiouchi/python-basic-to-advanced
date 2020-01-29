"""
Random Module

- In Python, it is another files to Python

Random Module -> there are many functions to generate

# Way 1 - import all module
# import random
# random() -> random number between 0 and 1

# all the functions, attributes, classes and properties will be in memory
# not recommended

# Way 2 - package and function name - Specific function to import
# random() function is different of random package

from random import random

for i in range(10):
    print(random(), end=", ")
# 0.48385530168903934, 0.9163770110849963, 0.8735984391116072, 0.13219961698619398, 0.040488465346551705,
# 0.8136847536634984, 0.07379661584552832, 0.6246814193670278, 0.21582976435052548, 0.910369576502084,

"""

# uniform() -> Generate value specifics

from random import uniform

for i in range(10):
    print(uniform(3, 7), end=", ")

# 5.076955559535821, 6.646886527159156, 4.316080894311492, 4.367959718171292, 6.551063773585145, 4.022643987622208,
# 5.088909105310803, 3.458080384848481, 6.745528670333863, 6.807443119388507,

# randint() -> Generate value specifics
print()

from random import randint

# Generate
for i in range(6):
    print(randint(1, 61), end=", ")
# 27, 37, 3, 42, 15, 54,

# choice() -> Show random value between iterables

from random import choice

players = ['stone', 'paper', 'scissor']
print(choice(players))  # choice one of them

print(choice('Yumi Ouchi'))  # choice one of them

# shuffle -> has data shuffle
from random import shuffle
cards = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8']

print(cards)  # ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8']
print(shuffle(cards))  # shuffle values
print(cards[0])  # first value
print(cards[10])  # last value
print(cards.pop())  # last value

