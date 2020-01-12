
# Lists

# lists inn python works like array (vector/matrix),
# the difference between another language that be dynamics and can be any data type.

# C or Java Language
#     - Fix size and type
#     or wise, if you create array with integer type with size 5, than the array is ALWAYS integer type and max size 5.
# Python language:
#     - Dynamic: Not has fix size, can create the list simple s and add elements with the memory (RAM) size.
#     - data type: any type.
#
# Lists are represented as brackets: []

print(type([]))

list_one = [1, 99, 3, 5, 6, 230, 40]

list_two = ['Y', 'u', 'm', 'i']

list_three = []

list_four = list(range(11))

list_five = list("Yumi")

# check the item is inside list.
num = 8
if num in list_four:
    print(f'{num} is inside')
else:
    print(f'{num} is not inside')

letter = 'ui'
if letter in list_five:
    print(f'{letter} is inside')
else:
    print(f'{letter} is not inside')

# We can sort easily
list_one.sort()
print(list_one)

# count the number of occurrences
print(list_one.count(2))
print(list_two.count('Y'))

# Add item the list: append

print(list_one)  # [1, 3, 5, 6, 40, 99, 230]
list_one.append(2)  # one element
print(list_one)  # [1, 3, 5, 6, 40, 99, 230, 2]

# OBS: The append has one argument
# list_one.append(12, 54, 11) # Error
list_one.append([8, 3, 1])  # [1, 3, 5, 6, 40, 99, 230, 2, [8, 3, 1]] -> add all elements
print(list_one)

sublist = [8, 3, 1]  # [8, 3, 1] is not inside
if letter in list_one:
    print(f'{sublist} is inside')
else:
    print(f'{sublist} is not inside')

# many elements
list_one.extend([123, 44, 67])  # [1, 3, 5, 6, 40, 99, 230, 2, [8, 3, 1], 123, 44, 67] -> single element
print(list_one)

list_one.extend('Yumi')
print(list_one)


# Can add item by index
# OBS: It not replace the start value
list_one.insert(2, "New world")  # -> [1, 99, 'New world', 3, 5, 6, 230, 40]
print(list_one)


list_six = list_one + list_two
print(list_six)
list_one = list_one + list_two
print(list_one)


# Way ONE
# Can easily reverse the list
list_one.reverse()
print(list_one)

# Way TWO
# OR Can easily reverse the list
print(list_two[::-1])


# Copy list
list_six = list_two.copy()
print(list_six)

# count the number of elements
print(len(list_two))  # 4
print(len(list_three))  # 0

# Remove and return the element removed
print(list_five)  # ['Y', 'u', 'm', 'i']
removed_element = list_five.pop()
print(removed_element, list_five)  # i ['Y', 'u', 'm']

# Can remove by index
# OBS: The elements to right index will be moved left
# OBS; if not exist the element at list will show the exception IndexError
print(list_one)  # [1, 99, 3, 5, 6, 230, 40]
list_one.pop(2)
print(list_one)  # [1, 99, 5, 6, 230, 40]

# Clear list - remove all elements
print(list_five)  # ['Y', 'u', 'm', 'i']
list_five.clear()
print(list_five)  # []

# Repeat easily the elements in the list
print(list_two)  # ['Y', 'u', 'm', 'i']
list_two = list_two * 3
print(list_two)  # ['Y', 'u', 'm', 'i', 'Y', 'u', 'm', 'i', 'Y', 'u', 'm', 'i']

# Can easily convert string to list
# Sample 1

master_degree = 'Machine Learning'
print(master_degree)  # Machine Learning
master_degree = master_degree.split()
print(master_degree)  # ['Machine', 'Learning']

# OBS: Standard, the split separate the element between spaces

master_degree = 'Machine,Learning,intelligence,artificial'
print(master_degree)  # Machine,Learning,intelligence,artificial
master_degree = master_degree.split(',')
print(master_degree)  # ['Machine', 'Learning', 'intelligence', 'artificial']

# Convert list to string
list_six = ['Machine', 'Learning', 'intelligence', 'artificial']
print(list_six)  # ['Machine', 'Learning', 'intelligence', 'artificial']

# Take the spaces between each element and transform in string
master_degree = " ".join(list_six)
print(master_degree)  # Machine Learning intelligence artificial

# transform just one string
master_degree = "$".join(list_six)
print(master_degree)  # Machine$Learning$intelligence$artificial

list_six = [1, 2.34, True, 'Geek', 'd', [1,2,3], 43523532452345]  # [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 43523532452345]
print(list_six)
print(type(list_six))  # <class 'list'>

# list iteration

# Sample 1 - FOR
soma = 0
for element in list_four:
    print(element, end=', ')
    soma = soma + element
print(soma)

#  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55

# Sample 2 - WHILE
car = []
product = ''

while product != 'exit':
    print("Add product or write exit")
    product = input()
    if product != 'exit':
        car.append(product)

for product in car:
    print(product)

# List variable

numbers = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numbers = [num1, num2, num3, num4, num5]
print(numbers)  # [1, 2, 3, 4, 5]

# list we cand o index way

#            0       1         2        3
colors = ['green', 'white', 'yellow', 'blue']
print(colors[0])  # green
print(colors[1])  # white
print(colors[2])  # yellow
print(colors[3])  # blue

# Inverse index
# Think the list like a circle
print(colors[-1])  # blue
print(colors[-2])  # yellow
print(colors[-3])  # white
print(colors[-4])  # green
# print(colors[-5])  # Error, not exist -5

colors = ['green', 'white', 'yellow', 'blue']

for color in colors:
    print(color)
index = 0

while index < len(colors):
    print(colors[index])
    index = index + 1

# index generate
for index, color in enumerate(colors):
    print(index, color)

# List accept repeated items
list = []
list.append(42)
list.append(42)
list.append(33)
list.append(33)
list.append(42)
list.append(42)

print(list)  # [42, 42, 33, 33, 42, 42]

# Utils methods
numbers = [5, 6, 7, 8, 9, 10, 5]
print(numbers.index(6))  # 1
print(numbers.index(9))  # 4
# if not exist show Error
# print(numbers.index(20))  # ValueError: 20 is not in list
print(numbers.index(5))  # 0 just the first item found

# after index 1
print(numbers.index(5, 1))  # 6 after 1
print(numbers.index(5, 3))  # 6 after 3
# print(numbers.index(20, 2))  # ValueError: 20 is not in list

# Search between range
print(numbers.index(8, 3, 6), end=", ")
print(numbers)
# Slicing revision

# list[start:end:step]
# range(start:end:step)

# Start parameters
numbers = [1, 2, 3, 4, 5]
print(numbers[1:])  # [2, 3, 4, 5] => start at 1 until end
print(numbers[1])  # 2
print(numbers[3:])  # [4, 5]

# End parameters
print(numbers[:2])  # [1, 2] => index -1
print(numbers[:4])  # [1, 2, 3, 4] => index -1

print(numbers[1:4])  # [2, 3, 4] => index -1

# STEP parameters
print(numbers[1::2])  # [2, 4]
print(numbers[::2])  # [1, 3, 5]
print(numbers[1::-1])  # [2, 1]
print(numbers[::-1])  # [5, 4, 3, 2, 1]

# Invert Sentence
names = ['Yumi', 'Ouchi']
names[0], names[1] = names[1], names[0]  # ['Ouchi', 'Yumi']
print(names)
names = ['Yumi', 'Ouchi']  # ['Ouchi', 'Yumi']
names.reverse()
print(names)
# Sum , max value, min value and size

# If the value is all integer or real
numbers = [1, 2, 3, 4, 5]

print(sum(numbers))  # 15
print(max(numbers))  # 5
print(min(numbers))  # 1
print(len(numbers))  # 5

# Transform list in tuple

numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
print(type(numbers))  # <class 'list'>

tuple_number = tuple(numbers)
print(tuple_number)  # (1, 2, 3, 4, 5)
print(type(tuple_number))  # <class 'tuple'>

# Unpack

numbers = [1, 2, 3]
num1, num2, num3 = numbers
print(num1)  # 1
print(num2)  # 2
print(num3)  # 3

# OBS: Unpack - number different of elements => Value Error
# Copy list to another (Shallow Copy and Deep Copy)

# Way 1 - Deep Copy
numbers = [1, 2, 3]
print(numbers)  # [1, 2, 3]

new_numbers = numbers.copy()  # copy
print(new_numbers)  # [1, 2, 3]

new_numbers.append(4)
print(numbers)  # [1, 2, 3]
print(new_numbers)  # [1, 2, 3, 4]

# list.copy() => independent list (not change another => Deep Copy)

# Way 2 - Shallow Copy
numbers = [1, 2, 3]
print(numbers)  # [1, 2, 3]

new_numbers = numbers  # copy
print(new_numbers)  # [1, 2, 3]

new_numbers.append(4)
print(numbers)  # [1, 2, 3, 4]
print(new_numbers)  # [1, 2, 3, 4]

# copy by attribute -> after change the another list => both change together







