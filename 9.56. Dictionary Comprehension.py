"""
Dictionary Comprehension

Think:

List:
list_number = [1, 2, 3, 4]
Tuple:
tuple_number = (1, 2, 3, 4)  # 1, 2, 3, 4
Set:
set_number = {1, 2, 3, 4}
Dictionary:
dict_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Syntax
{key: value for value in iteration}

# Sample 1
dict_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quad = {key: value ** 2 for key, value in dict_number.items()}

print(dict_number.items())  # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(quad)  # {'a': 1, 'b': 4, 'c': 9, 'd': 16}

# List
list_number = [1, 2, 3, 4]

quad = {value: value ** 2 for value in list_number}
print(quad)  # {1: 1, 2: 4, 3: 9, 4: 16}

# Tuple
tuple_number = (1, 2, 3, 4)  # 1, 2, 3, 4

quad = {value: value ** 2 for value in tuple_number}
print(quad)  # {1: 1, 2: 4, 3: 9, 4: 16}

# Set
set_number = {1, 2, 3, 4}

quad = {value: value ** 2 for value in set_number}
print(quad)  # {1: 1, 2: 4, 3: 9, 4: 16}

# List Repeat item
list_number = [1, 2, 3, 4, 1, 2]

quad = {value: value ** 2 for value in list_number}
print(quad)  # {1: 1, 2: 4, 3: 9, 4: 16}

keys = 'abcde'
values = [1, 2, 3, 4, 5]

miss_dict = {keys[i]: values[i] for i in range(len(keys))}
print(miss_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

"""

# Sample conditional logic
values = [1, 2, 3, 4, 5]
result = {value: ('even' if value % 2 == 0 else 'odd') for value in values}
print(result)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}


