"""
Set Comprehension

List uses [] repeated and Ordered
Set uses {} Not repeated and Not Ordered

"""
# Samples
numbers = {num for num in range(1, 7)}
print(numbers)  # {1, 2, 3, 4, 5, 6}

# Other Sample
numbers = {num ** 2 for num in range(10)}
print(numbers)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# OBS: Make alteration at structure to generate a dictionary

# Dictionary
numbers = {num: num ** 2 for num in range(10)}
print(numbers)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

characters = {character for character in 'Yumi Yumi Ouchi'}
print(characters)  # {'i', 'h', 'u', 'O', ' ', 'Y', 'c', 'm'}


