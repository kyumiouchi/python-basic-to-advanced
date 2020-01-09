"""
Reversed

OBS: It is different from reverse() from list => the function reverse() just work with
list and reversed() with any iterable.
"""
list_number = [1, 2, 3, 4, 5]

result = reversed(list_number)

print(result)  # <list_reverseiterator object at 0x0000029BC4B12FD0>
print(type(result))  # <class 'list_reverseiterator'>

# Convert List, Tuple and Set

# List
print(list(reversed(list_number)))  # [5, 4, 3, 2, 1]

# Tuple
print(tuple(reversed(list_number)))  # (5, 4, 3, 2, 1)

# Set
print(set(reversed(list_number)))  # {1, 2, 3, 4, 5} # not define order of the elements

for character in reversed('Geek University'):  # ytisrevinU keeG
    print(character, end='')

print('\n')

print(''.join(list(reversed('Geek University'))))  # ytisrevinU keeG

# the same as slice of strings
print('Yumi Ouchi'[::-1])  # ihcuO imuY

# reversed() to loop reversed
for item in reversed(range(0, 10)):  # 9876543210
    print(item, end='')

print('\n')

# range does too
for item in range(9, -1, -1):  # 9876543210
    print(item, end='')
