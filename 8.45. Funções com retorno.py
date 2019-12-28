"""
Return functions

number = [1, 2, 3]
return_value = number.pop()
print(f'retun of pop:{return_value}')

OBS: when return value not exist, return None

OBS: 'return' return value

OBS: execute return with other function


def quad_7():
    return 7 * 7


return_value = quad_7()  # 49
print(return_value)  # 49

print(quad_7())  # 49


def said_hello():
    return 'Hello'


somebody = 'Yumi'

print(said_hello())  # Hello
print(somebody)  # Yumi

# OBS: return reserved word

Return:
1 - Finish the function and get out execution
2 - It can have Differents returns
3 - It can have differents type and multiple values


# Sample 1
def function_helper():
    print('Before Hi', end=', ')
    return 'Hi'
    print('After Hi')


print(function_helper())  # Before Hi, Hi


# Sample 2
def function_helper():
    variable = True
    if variable:
        return 4
    elif variable is None:
        return 3.2
    return 'Hi'

print(function_helper())  # 4


# Sample 3
def other_function():
    return 2, 3, 4, 5


num1, num2, num3, num4 = other_function()

print(num1, num2, num3, num4)  # 2 3 4 5

from random import random


def play_flip_coin():
    if random() > 0.5:
        return 'Heads'
    return 'Tails'


print(play_flip_coin())
"""


# Unnecessary

def odd():
    number = 5
    if number % 2 != 0:
        return True
    return False


print(odd())  # True
