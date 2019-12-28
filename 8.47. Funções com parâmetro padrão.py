"""
Standard parameter functions

    - Optional parameters functions

print('Yumi Ouchi')  # Yumi Ouchi
print()  # (empty)


def quad(number):
    return number ** 2


print(quad(3))  # 9


# print(quad())  # TypeError: quad() missing 1 required positional argument: 'number'


def exponential(number=4, potential=2):
    return number ** potential


print(exponential(2, 3))  # 8
print(exponential(3, 2))  # 9


print(exponential(3))  # 9  # first and second parameter are optional
print(exponential(3, 5))  # 243
print(exponential())  # 16

# ERROR = value default MUST be in the end of parameters
def test(num=2, potential):
    return num ** potential

def sum(num1=4, num2=3):
    return num1 + num2


print(sum(4, 3))


# print(sum(4))  # TypeError: sum() missing 1 required positional argument: 'num2'
# print(sum())  # TypeError: sum() missing 2 required positional arguments: 'num1' and 'num2'

def show_information(name='Geek', instructor=False):
    if name == 'Geek' and instructor:
        return 'Welcome instructor Geek'
    elif name == 'Geek':
        return 'I thought you was a instructor'
    return f'Hello {name}'


print(show_information())  # I thought you was a instructor
print(show_information(instructor=True))  # Welcome instructor Geek
print(show_information(True))  # Hello True
print(show_information('Ozzy'))  # Hello Ozzy
print(show_information(name='Yumi'))  # Hello Yumi


# Which kind of parameters com be?

# Any type
#   - Number, strings, floats, booleans, lists, tuples, dictionaries, functions and etc...

# Sample function as parameter

def sum(num1, num2):
    return num1 + num2
def mat(num1, num2, fun = sum):
    return fun(num1, num2)
def subtraction(num1, num2):
    return num1 - num2

print(mat(1, 2))  # 3
print(mat(1, 2, subtraction))  # -1

# Scope = Avoid problems and confusion

# Global variable
# Local Variable

instructor = 'Yumi'

def hello():
    instructor = 'Python'
    return f'Hello {instructor}'

print(hello())  # Hello Python

# OBS: If var global is the same name of var local then local has preference

def hello():
    professor = 'Python'
    return f'Hello {professor}'

print(hello())  # Hello Python
# print(professor)  # NameError: name 'professor' is not defined
# If can avoid GLOBAL var is better
total = 0


def increase():
    global total  # Use variable global
    total = total + 1
    return total


print(increase())  # UnboundLocalError: local variable 'total' referenced before assignment
# Variable is not started
print(increase())  # 2
print(increase())  # 3
"""

def out():
    count = 0

    def inside():
        nonlocal count  # not global and not local (function before)
        count = count + 1
        return count
    return inside()

print(out())  # 1
print(out())  # 1
print(out())  # 1

# print(inside())  # NameError: name 'inside' is not defined
