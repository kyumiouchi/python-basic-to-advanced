"""
Tuple

Exist tuples are very close to list.

Two differences basics:
1 - Tuples are represent by parentheses ()
2 - Tuples are unchanging

list_number = [1, 5, 3, 4, 2]
list_number.sort()
print(list_number)  # [1, 2, 3, 4, 5]

# WARNING 1
tuple_one = (1, 2, 3, 4, 5)
print(tuple_one)  # (1, 2, 3, 4, 5)
print(type(tuple_one))  # <class 'tuple'>


tuple_two = 1, 2, 3, 4, 5
print(tuple_two)  # <class 'tuple'>
print(type(tuple_two))  # (1, 2, 3, 4, 5)

# WARNING 2: One element

tuple_three = (4)
print(tuple_three)  # 4
print(type(tuple_three))  # <class 'int'>

tuple_three = (4,)
print(tuple_three)  # (4,)
print(type(tuple_three))  # <class 'tuple'>

tuple_four = 4,
print(tuple_four)  # (4,)
print(type(tuple_four))  # <class 'tuple'>

# CONCLUSION: Tuple is defined by by comma

(4) -> not tuple
(4, ) -> Tuple
4, -> Tuple

# Can create dynamically
tuple_number = tuple(range(11))
print(tuple_number)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(tuple_number))  # <class 'tuple'>

# Unpack Tuple
tuple_all = ('GeeK Yumi', 'Game developer',)
name, profession = tuple_all

print(name)  # GeeK Yumi
print(profession)  # Game developer

# ERROR: number different to UNPACK size

# Method to add or remove element not exist, because it is unchanging
# If value is integer or real you can sum, min, max

tuple_number = 1, 2, 3, 4, 5, 'b'
print(type(tuple_number))  # <class 'tuple'>
# print(sum(tuple_number))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(min(tuple_number))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(max(tuple_number))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(len(tuple_number))  # 6
"""
# Tuple concatenated
tuple_one = (1, 2, 3)
print(tuple_one)  # (1, 2, 3)

tuple_two = (4, 5, 6)
print(tuple_two)  # (4, 5, 6)

print(tuple_one + tuple_two)  # (1, 2, 3, 4, 5, 6)
print(tuple_one)  # (1, 2, 3)
print(tuple_two)  # (4, 5, 6)

tuple_three = tuple_one + tuple_two  # unchanging, but can overwrite the value

print(tuple_three)  # (1, 2, 3, 4, 5, 6)
print(tuple_one)  # (1, 2, 3)
print(tuple_two)  # (4, 5, 6)

tuple_one = tuple_one + tuple_two  # unchanging, but can overwrite the value
print(tuple_one)  # (1, 2, 3, 4, 5, 6)
print(tuple_two)  # (4, 5, 6)

