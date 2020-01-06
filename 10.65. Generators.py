"""
Generators Expression

WE studied:
    - List Comprehension
    - Dictionary Comprehension
    - Set Comprehension

Not use:
    - Tuple Comprehension => because call Generators

# List Comprehension
names = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina', 'Vanessa']
print(any([name[0] == 'C' for name in names]))  # True

# Generator => Less resource of memory computer
names = ['Carlos', 'Camila', 'Carla', 'Cassino', 'Cristina', 'Vanessa']
print(any((name[0] == 'C' for name in names)))  # True

# List Comprehension
result = [name[0] == 'C' for name in names]
print(type(result))  # <class 'list'>
print(result)  # [True, True, True, True, True, False]

# Generator => Less resource of memory computer
result = (name[0] == 'C' for name in names)
print(type(result))  # <class 'generator'>
print(result)  # print(result)  #

# import sys
# getsizeof => quantity of size in byte at memory
from sys import getsizeof

print(getsizeof('Yumi'))  # 53
print(getsizeof('Yumi Ouchi'))  # 59
print(getsizeof(9))  # 28
print(getsizeof(91))  # 28
print(getsizeof(1234123412))  # 32
print(getsizeof(True))  # 28

list_comp = getsizeof([x * 10 for x in range(1000)])

set_comp = getsizeof({x * 10 for x in range(1000)})

dict_comp = getsizeof({x:x * 10 for x in range(1000)})

gen_comp = getsizeof(x * 10 for x in range(1000))

print("Memory:")
print(f'List Comprehension: {list_comp}')  # 9024
print(f'Set Comprehension: {set_comp}')  # 32992
print(f'Dictionary Comprehension: {dict_comp}')  # 36968
print(f'Generator: {gen_comp}')  # 88
"""

gen_comp = (x * 10 for x in range(1000))
print(gen_comp)  # <generator object <genexpr> at 0x000001484F2CFD58>
print(type(gen_comp))  # <class 'generator'>

for number in gen_comp:
    print(number)
