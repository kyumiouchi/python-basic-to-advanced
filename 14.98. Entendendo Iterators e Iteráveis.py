"""
Understanding Iterators and iterables

Iterator ->
    - Object os program that it can iterable.
    - return one data, when each element is called with next().

Iterable ->
    - Object will return a iterable when iter() function is called.

name = 'Geek'  # it is iterable, but not iterator
numbers = [1, 2, 3, 4, 5, 6]  # it is iterable, but not iterator

name_iterator = iter(name)  # iterator
numbers_iterator = iter(numbers)  # iterator

print(next(name_iterator))  # G
print(next(name_iterator))  # e
print(next(name_iterator))  # e
print(next(name_iterator))  # k
# print(next(name_iterator))  # StopIteration

print(next(numbers_iterator))  # 1
print(next(numbers_iterator))  # 2
print(next(numbers_iterator))  # 3
print(next(numbers_iterator))  # 4
print(next(numbers_iterator))  # 5
print(next(numbers_iterator))  # 6
# print(next(numbers_iterator))  # StopIteration
"""
name = 'Geek'  # it is iterable, but not iterator

for character in name:
    print(f'{character}', end=", ")  # G, e, e, k,

[print(f'{character}', end=", ") for character in name]
