"""
List Comprehension - Part 1

 - Using List comprehension we can generate new lists with process data to another iteration

 # Syntax
[ data for data in iteration ]
# Sample 1
numbers = [1, 2, 3, 4, 5]
result = [number * 10 for number in numbers]
print(result)  # [10, 20, 30, 40, 50]

To understand better

- first part = for number in numbers
- second part = number * 10

# Sample 2
result = [number / 2 for number in numbers]
print(result)  # [0.5, 1.0, 1.5, 2.0, 2.5]

def my_function(value):
    return value * value

result = [my_function(number) for number in numbers]
print(result)  # [1, 4, 9, 16, 25]

# List Comprehension X Loop
numbers = [1, 2, 3, 4, 5]

# Loop
number_double_list = []
for number in numbers:
    number_double_list.append(number * 2)
print(number_double_list)  # [2, 4, 6, 8, 10]

# List Comprehension
print([number * 2 for number in numbers])  # [2, 4, 6, 8, 10]
"""
# Other Sample

# 1
name = 'Yumi Ouchi'
print([character.upper() for character in name])  # ['Y', 'U', 'M', 'I', ' ', 'O', 'U', 'C', 'H', 'I']

# 2
def uppercase(name):
    name = name.replace(name[0], name[0].upper())
    return name

friends = ['dani', 'lulu', 'nana', 'jojo', 'gil', 'pina']
print([uppercase(friend) for friend in friends])  # ['D', 'L', 'N', 'J', 'G', 'P']
print([friend.title() for friend in friends])  # ['D', 'L', 'N', 'J', 'G', 'P']

# 3
print([number * 2 for number in range(1, 11)])  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 4
print([bool(value) for value in [0, [], '', True, 1, 3.14]])
# [False, False, False, True, True, True]

# 5
print([str(value) for value in [1, 2, 3, 4, 5]])
# ['1', '2', '3', '4', '5']



