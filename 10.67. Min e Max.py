"""
Min and Max

max() -> the biggest number

list_sample = [1, 8, 4, 99, 34, 129]
print(max(list_sample))  # 129

tuple_sample = (1, 8, 4, 99, 34, 129)
print(max(tuple_sample))  # 129

set_sample = {1, 8, 4, 99, 34, 129}
print(max(set_sample))  # 129

dict_sample = {'a': 1, 'b':  8, 'c':   4, 'd':   99, 'e':   34, 'f':   129}
print(max(dict_sample))  # f

dict_sample = {'a': 1, 'b':  8, 'c':   4, 'd':   99, 'e':   34, 'f':   129}
print(max(dict_sample.values()))  # 129

# Do a  program with two value and sho the max
value_one = int(input('Write the first value: '))
value_two = int(input('Write the second value: '))

print(max(value_one, value_two))

print(max(4, 67, 54))  # 67
print(max('a', 'ab', 'abc'))  # abc
print(max('a', 'b', 'c', 'g'))  # g
print(max(4.4353, 5.3453))  # 5.3453
print(max('Yumi Ouchi'))  # u

min() -> the minor value

list_sample = [1, 8, 4, 99, 34, 129]
print(min(list_sample))  # 1

tuple_sample = (1, 8, 4, 99, 34, 129)
print(min(tuple_sample))  # 1

set_sample = {1, 8, 4, 99, 34, 129}
print(min(set_sample))  # 1

dict_sample = {'a': 1, 'b':  8, 'c':   4, 'd':   99, 'e':   34, 'f':   129}
print(min(dict_sample))  # a

dict_sample = {'a': 1, 'b':  8, 'c':   4, 'd':   99, 'e':   34, 'f':   129}
print(min(dict_sample.values()))  # 1

# Do a  program with two value and sho the max
value_one = int(input('Write the first value: '))
value_two = int(input('Write the second value: '))

print(min(value_one, value_two))

print(min(4, 67, 54))  # 4
print(min('a', 'ab', 'abc'))  # a
print(min('a', 'b', 'c', 'g'))  # a
print(min(4.4353, 5.3453))  # 4.4353
print(min('Yumi Ouchi'))  # ' '
names = ['Anat', 'Samson', 'Zanpy', 'Robervaldeck', 'Tim']
print(max(names))  # Zanpy
print(min(names))  # Anat
print(max(names, key=lambda name: len(name)))  # Robervaldeck
print(min(names, key=lambda name: len(name)))  # Tim
"""
musics = [
    {"title": "Thunderstruck", "sing": 3},
    {"title": "Dead Bla", "sing": 2},
    {"title": "Back Bla", "sing": 4},
    {"title": "Too old bla", "sing": 32},
]

print(max(musics, key=lambda music: music['sing']))  # {'title': 'Too old bla', 'sing': 32}
print(min(musics, key=lambda music: music['sing']))  # {'title': 'Dead Bla', 'sing': 2}

# Challenge! Print just the title of music with max and min singed

print(max(musics, key=lambda music: music['sing'])['title'])  # Too old bla
print(min(musics, key=lambda music: music['sing'])['title'])  # Dead Bla

# Challenge! Print the same without max(), min() and lambda
max = 0
for music in musics:
    if music['sing'] > max:
        max = music['sing']

for music in musics:
    if music['sing'] == max:
        print("max", music['title'])  # max Too old bla

min = 99999
for music in musics:
    if music['sing'] < min:
        min = music['sing']

for music in musics:
    if music['sing'] == min:
        print("min", music['title'])  # min Dead Bla