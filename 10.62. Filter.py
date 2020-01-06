"""
# Filter

# filter() -> filter data from collection

import statistics  # work with statistics data

values = 1, 2, 3, 4, 5, 6

medium = (sum(values) / len(values))
print(medium)  # 3.5

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# medium of statistics
medium = statistics.mean(data)
print(medium)  # 2.183333333333333

# OBS: as like map(), receive two parameters, function and iteration
result = filter(lambda x: x > medium, data)
print(list(result))  # [2.7, 4.1, 4.3]

result = filter(lambda x: x < medium, data)
print(type(result))  # <class 'filter'>
print(list(result))  # [1.3, 0.8, -0.1]
print(f'Again: {list(result)}')  # []

# OBS: after used the information is cleaned


countries = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(countries)
# ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

result = filter(None, countries)
print(list(result))
# ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']

result = filter(lambda country: len(country) > 0, countries)
print(list(result))
# ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']

result = filter(lambda country: country != "", countries)
print(list(result))
# ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']

# Difference between map and filter:
# map() -> 2 parameters => return iterable object or True or False
# filter() -> 2 parameters => return just the object result True

# Sample complex

users = [
    {"username": "samuel", "tweet": ["I love cakes", "I love pizza"]},
    {"username": "carlla", "tweet": ["I love cats"]},
    {"username": "jeff", "tweet": []},
    {"username": "bob", "tweet": []},
    {"username": "goggo", "tweet": ["I love dogs", "I am going out today"]},
    {"username": "gal", "tweet": []}
]
print(users)
# [{'username': 'samuel', 'tweet': ['I love cakes', 'I love pizza']}, {'username': 'carlla', 'tweet': ['I love
# cats']}, {'username': 'jeff', 'tweet': []}, {'username': 'bob', 'tweet': []}, {'username': 'goggo', 'tweet': ['I
# love dogs', 'I am going out today']}, {'username': 'gal', 'tweet': []}]

# Filter the unavailable Twitter

# Way 1
unavailable = list(filter(lambda u: len(u["tweet"]) == 0, users))
print(unavailable)
# [{'username': 'jeff', 'tweet': []}, {'username': 'bob', 'tweet': []}, {'username': 'gal', 'tweet': []}]

unavailable = list(map(lambda u: len(u["tweet"]) == 0, users))
print(unavailable)
# [False, False, True, True, False, True]

unavailable = list(filter(lambda u: not u["tweet"], users))  # len(u["tweet"]) == 0
print(unavailable)
# [{'username': 'jeff', 'tweet': []}, {'username': 'bob', 'tweet': []}, {'username': 'gal', 'tweet': []}]

"""
# Combine filter() and map()

names = ['Yumi', 'Suzana', 'Mari']

# Create a list if contains 5 character

list_value = list(map(lambda name: f'Your instructor is {name}', filter(lambda name: len(name) < 5, names)))
print(list_value)
# ['Your instructor is Yumi', 'Your instructor is Mari']












