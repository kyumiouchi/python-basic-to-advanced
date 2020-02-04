"""
Create your own loop version

for num in [1, 2, 3, 4, 5]:
    print(num, end=", ")  # 1, 2, 3, 4, 5,

print()

for character in 'Yumi Ouchi':
    print(character, end=", ")  # Yumi Ouchi,

iter([1, 2, 3, 4, 5])
iter('Yumi Ouchi')
"""


def my_for(iterable):
    iterable_help = iter(iterable)
    while True:
        try:
            print(next(iterable_help), end=", ")
        except StopIteration:
            print()
            break


my_for('Yumi Ouchi')  # Y, u, m, i,  , O, u, c, h, i,
numbers = [1, 2, 3, 4, 5]  # 1, 2, 3, 4, 5,
my_for(numbers)
