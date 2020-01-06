"""
Sorted

OBS: It is different of sort() of List.
Sorted => Can sort N iterable.

OBS: sorted ALWAYS return a LIST

list_number = [1, 4, 6, 2, 1]
print(list_number)  # [1, 4, 6, 2, 1]
print(sorted(list_number))  # [1, 1, 2, 4, 6]
print(list_number)  # [1, 4, 6, 2, 1]

set_number = {1, 4, 6, 2, 1}
print(sorted(set_number))  # [1, 2, 4, 6]

print(sorted(list_number, reverse=True))  # [6, 4, 2, 1, 1]

print(tuple(sorted(list_number, reverse=True)))  # (6, 4, 2, 1, 1)

print(set(sorted(list_number, reverse=True)))  # {1, 2, 4, 6}

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
# love dogs', 'I am going out today']}, {'username': 'gal', 'tweet': []}] print(sorted(users))  # TypeError: '<' not
# supported between instances of 'dict' and 'dict'

print(sorted(users, key=len))
# [{'username': 'samuel', 'tweet': ['I love cakes', 'I love pizza']}, {'username': 'carlla', 'tweet': ['I love
# cats']}, {'username': 'jeff', 'tweet': []}, {'username': 'bob', 'tweet': []}, {'username': 'goggo', 'tweet': ['I
# love dogs', 'I am going out today']}, {'username': 'gal', 'tweet': []}]


users = [
    {"username": "samuel", "tweet": ["I love cakes", "I love pizza"]},
    {"username": "carlla", "tweet": ["I love cats"]},
    {"username": "jeff", "tweet": []},
    {"username": "bob", "tweet": [], "cor": "yellow"},
    {"username": "goggo", "tweet": ["I love dogs", "I am going out today"]},
    {"username": "gal", "tweet": [], "cor": "black", "music": "Rock"}
]

print(sorted(users, key=len))  # nothing happen
# [{'username': 'samuel', 'tweet': ['I love cakes', 'I love pizza']}, {'username': 'carlla', 'tweet': ['I love
# cats']}, {'username': 'jeff', 'tweet': []}, {'username': 'goggo', 'tweet': ['I love dogs', 'I am going out
# today']}, {'username': 'bob', 'tweet': [], 'cor': 'yellow'}, {'username': 'gal', 'tweet': [], 'cor': 'black',
# 'music': 'Rock'}]

print(sorted(users, key=lambda user: user["username"]))
# [{'username': 'bob', 'tweet': [], 'cor': 'yellow'}, {'username': 'carlla', 'tweet': ['I love cats']}, {'username':
# 'gal', 'tweet': [], 'cor': 'black', 'music': 'Rock'}, {'username': 'goggo', 'tweet': ['I love dogs', 'I am going
# out today']}, {'username': 'jeff', 'tweet': []}, {'username': 'samuel', 'tweet': ['I love cakes', 'I love pizza']}]

print(sorted(users, key=lambda user: user["tweet"]))
# [{'username': 'jeff', 'tweet': []}, {'username': 'bob', 'tweet': [], 'cor': 'yellow'}, {'username': 'gal',
# 'tweet': [], 'cor': 'black', 'music': 'Rock'}, {'username': 'samuel', 'tweet': ['I love cakes', 'I love pizza']},
# {'username': 'carlla', 'tweet': ['I love cats']}, {'username': 'goggo', 'tweet': ['I love dogs', 'I am going out
# today']}]

print(sorted(users, key=lambda user: len(user["tweet"])))
# [{'username': 'jeff', 'tweet': []}, {'username': 'bob', 'tweet': [], 'cor': 'yellow'}, {'username': 'gal',
# 'tweet': [], 'cor': 'black', 'music': 'Rock'}, {'username': 'carlla', 'tweet': ['I love cats']}, {'username':
# 'samuel', 'tweet': ['I love cakes', 'I love pizza']}, {'username': 'goggo', 'tweet': ['I love dogs', 'I am going
# out today']}]
"""

musics = [
    {"title": "Thunderstruck", "sing": 3},
    {"title": "Dead Bla", "sing": 2},
    {"title": "Back Bla", "sing": 4},
    {"title": "Too old bla", "sing": 32},
]

print(sorted(musics, key=lambda music: music['sing']))
# [{'title': 'Dead Bla', 'sing': 2}, {'title': 'Thunderstruck', 'sing': 3}, {'title': 'Back Bla', 'sing': 4},
# {'title': 'Too old bla', 'sing': 32}]
print(sorted(musics, key=lambda music: music['sing'], reverse=True))
# [{'title': 'Too old bla', 'sing': 32}, {'title': 'Back Bla', 'sing': 4}, {'title': 'Thunderstruck', 'sing': 3},
# {'title': 'Dead Bla', 'sing': 2}]
