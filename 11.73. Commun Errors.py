"""
Common Errors

It is important to understand the error code

SyntaxError - Syntax error- not part of Python language
"""

# printf('Geek University')  # NameError: name 'printf' is not defined
# print('Geek University')

# 1) Syntax Error

# 1
# def function:  # SyntaxError: invalid syntax
#     print('Geek University')

# 2
# None = 1  # SyntaxError: can't assign to keyword

# 3
# return  # SyntaxError: 'return' outside function

# 2) Name Error -> Variable or Function is not defined

# a.
# print(geek)  # NameError: name 'geek' is not defined

# b.
# geek()  # NameError: name 'geek' is not defined

# c.
# a = 18
#
# if a < 10:
#     msg = 'Is great than 10'
#
# print(msg)  # NameError: name 'msg' is not defined

# 3 - Type Error -> function/operation/action

# a.
# print(len(5))  # TypeError: object of type 'int' has no len()

# b.
# print('Geek' + [])  # TypeError: must be str, not list

# 4 - IndexError - element of list wrong and or index data type

# list_n = ['Geek']
# a.
# print(list_n[2])  # IndexError: list index out of range

# b.
# print(list_n[0][10])  # IndexError: list index out of range

# tuple_n = ('Geek',)
# print(tuple_n[0][10])  # IndexError: string index out of range

# 5) Value Error -> function/operation build-in argument with wrong type

# Smaples
# a.
# print(int('42'))
# print(int('GEek'))  # ValueError: invalid literal for int() with base 10: 'GEek'

# 6)  Key Error-> Happen when try to access a dictionary with a key that not exist
# a.
# dic = {}
# print(dic['geek'])  # KeyError: 'geek'

# 7) AttributeError -> variable do not have attribute/function
# a.
# tuple_n = (11, 2,  31, 4)
# print(tuple_n.sort())  # AttributeError: 'tuple' object has no attribute 'sort'

# 8) IndentationError -> not respect the indentation od 4 spaces
# a.
# def new_function():
# print("Geek")  # IndentationError: expected an indented block


# for i in range(10):
# i+1  # IndentationError: expected an indented block

# OBS: Exception == Error
# Important to read the output error
