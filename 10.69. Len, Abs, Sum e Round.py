"""
Len, Abs, Sum e Round

# Len
len() -> count the number of items

# Just to review
print(len('Geek University'))  # 15
print(len([1, 2, 3, 4, 5]))  # 5
print(len({1, 2, 3, 4, 5}))  # 5
print(len((1, 2, 3, 4, 5)))  # 5
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))  # 5

# It is the same as:

# Dunder len
print('Geek University'.__len__())  # 15

# Abs

abs() -> Return the absolute value without the signal
"""

# Sample Abs
print(abs(-5))  # 5
print(abs(5))  # 5
print(abs(3.14))  # 3.14
print(abs(-3.14))  # 3.14
# print(abs('Yumi'))  # TypeError: bad operand type for abs(): 'str'

# Sum

# sum() -> Sum all values

# OBS: the default is 0

print(sum([1, 2, 3, 4, 5]))  # 15
print(sum([1, 2, 3, 4, 5], 5))  # 20

print(sum([3.123, 4.243]))  # 7.3660000000000005
print(sum({1, 2, 3, 4, 5}))  # 15
print(sum((1, 2, 3, 4, 5)))  # 15
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))  # 15
# print(sum('Geek University'))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Round
# round() -> Return the N digits precision after the decimal. If not defined the precision than sho the more closed

print(round(10.2))  # 10
print(round(10.5))  # 10
print(round(10.6))  # 11
print(round(1.2121212121, 2))  # 1.21
print(round(1.21999999999, 2))  # 1.22
print(round(1.21999999999))  # 1

