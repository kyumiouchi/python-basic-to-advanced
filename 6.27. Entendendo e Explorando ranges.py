"""
Ranges


- we need to understand the loop to use ranges
- we need to know the range to understand better

Ranges are used to generate the numerical sequence, not random, but other way

General way;

# way 1
range(value)

OBS: start with 0 and go 1 by 1
# Way 1
for num in range(11):
    print(num)
# 0,1,2,3,4,5,6,7,8,9,10

# Way 2
range(start, end)

OBS: chose the start way and 1 by 1

# Way 2
for num in range(4, 11):
    print(num)

# 4,5,6,7,8,9,10

# Way 3
range(start, end, step)

# Way 3
for num in range(4, 11, 2):  # 4, 6, 8, 10
    print(num, end=", ")

# Way 4 (invert)

range(end, start, step)

OBS: regret to end to start by step bu step
# Way 4
for num in range(10, -1, -1):  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
    print(num, end=", ")
"""

# list
print(range(10))  # -> range(10)
print(range(2, 10))  # -> range(2, 10)
print(range(2, 10, 2))  # -> range(2, 10, 2)
list_range = list(range(10))
print(list_range)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
