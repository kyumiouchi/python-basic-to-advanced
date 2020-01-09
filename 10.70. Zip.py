"""
Zip

zip() -> Create a iterable (Zip object) to aggregate the elements to each iterable with paired input
"""

# Sample

list_number1 = [1, 2, 3]
list_number2 = [4, 5, 6]

zip1 = zip(list_number1, list_number2)
print(zip1)  # <zip object at 0x0000017183B9B588>
print(type(zip1))  # <class 'zip'>

# Always can generate a list, tuple, or dictionary

print(list(zip1))  # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]  # after execute...the zip1 is empty
zip1 = zip(list_number1, list_number2)
print(tuple(zip1))  # ((1, 4), (2, 5), (3, 6))
zip1 = zip(list_number1, list_number2)
print(set(zip1))  # {(2, 5), (3, 6), (1, 4)}
zip1 = zip(list_number1, list_number2)
print(dict(zip1))  # {1: 4, 2: 5, 3: 6}

list_number3 = [7, 8, 9, 10, 11]

zip2 = zip(list_number1, list_number2, list_number3)
print(list(zip2))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

zip2 = zip(list_number3, list_number2, list_number1)
print(list(zip2))  # [(7, 4, 1), (8, 5, 2), (9, 6, 3)]


# Different iterable with zip
tuple_number = 1, 2, 3, 4, 5
list_number = [6, 7, 8, 9, 10]
dict_number = {'a:': 11, 'b:': 12, 'c:': 13, 'd:': 14, 'e:': 15}
zip3 = zip(tuple_number, list_number, dict_number)
print(list(zip3))  # [(1, 6, 'a:'), (2, 7, 'b:'), (3, 8, 'c:'), (4, 9, 'd:'), (5, 10, 'e:')]

values = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*values)))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

test1 = [80, 91, 78]
test2 = [98, 89, 53]
students = ['maria', 'pedro', 'carla']

print(list(zip(students, test1, test2)))  # [('maria', 80, 98), ('pedro', 91, 89), ('carla', 78, 53)]

final = {value[0]: max(value[1], value[2]) for value in zip(students, test1, test2)}
print(final)  # {'maria': 98, 'pedro': 91, 'carla': 78}

# map()
final = zip(students, map(lambda score: max(score), zip(test1, test2)))

print(dict(final))  # {'maria': 98, 'pedro': 91, 'carla': 78}
