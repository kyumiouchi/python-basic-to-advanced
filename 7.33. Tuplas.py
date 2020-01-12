"""
Tuple

Exist tuples are very close to list.

Two differences basics:
1 - Tuples are represent by parentheses ()
2 - Tuples are unchanging
"""
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

# (4) -> not tuple
# (4, ) -> Tuple
# 4, -> Tuple

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

# element in tuple

tuple_one = (1, 2, 3)
print(3 in tuple_one)  # True
print(33 in tuple_one)  # False

# Tuple iteration
for n in tuple_one:
    print(n, end=', ')  # 1, 2, 3,

for index, value in enumerate(tuple_one):
    print(index, value, end=', ')  # 0 1, 1 2, 2 3,

# Count element at tuple
tuple_two = ('a', 'b', 'c', 'd', 'e', 'a', 'b', 'b')
print(tuple_two.count('c'))  # 1

tuple_yumi = tuple("Yumi Ouchi")
print(tuple_yumi)  # ('Y', 'u', 'm', 'i', ' ', 'O', 'u', 'c', 'h', 'i')

print(tuple_yumi.count('Y'))  # 1

# Tuple using

# Tuple ALWAYS not modified at collection

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

print(months)  # ('January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# Access is similar to list
print(months[5])  # July

# while iteration
i = 0
while i < len(months):
    print(months[i], end=', ')
    i += 1
# January, February, March, April, June, July, August, September, October, November, December,

# print(months.index('Playstation'))  # ValueError: tuple.index(x): x not in tuple
print(months.index('April'))  # 3
print(months.index('June', 4))  # 4

# slicing
# tuple[start:end:atep]
print(months[5:9])  # months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# Why use tuple?
#  - Faster then list
#  - Tuple code more secure
#  - Unchanging bring more secure

# Copy tuple to another
tuple_one = (1, 2, 3)
print(tuple_one)  # (1, 2, 3)

new_tuple = tuple_one  # Not have problem of Shallow Copy

tuple_two = (4, 5, 6)
print(tuple_two)  # (4, 5, 6)

tuple_one = tuple_one + tuple_two

print(tuple_one)  # (1, 2, 3, 4, 5, 6)
print(new_tuple)  # (1, 2, 3)

list_ = [1, ]
print(type(list_))  # <class 'list'>
list_ = 1,
print(type(list_))  # <class 'tuple'>
