"""
Collections - Named Tuple

Named tuple -> Difference from tuple, we specify the name of the parameter

# Tuple common
tuple_name = (1, 2, 3)
print(tuple_name)  # (1, 2, 3)
"""
from collections import namedtuple

# define parameter and type
# Way 1 -  defined named tuple
dog = namedtuple('dog', 'age race name')

# Way 2 -  defined named tuple
dog = namedtuple('dog', 'age, race, name')

# Way 3 -  defined named tuple
dog = namedtuple('dog', ['age', 'race', 'name'])

# Using
ray_dog = dog(age=2, race='Chow-Chow', name='Ray')

print(ray_dog)  # dog(age=2, race='Chow-Chow', name='Ray')

# Way 1
print(ray_dog[0])  # age
print(ray_dog[1])  # race
print(ray_dog[2])  # name
# Way 2
print(ray_dog.age)  # age
print(ray_dog.race)  # race
print(ray_dog.name)  # name

print(ray_dog.index('Chow-Chow'))  # index = 1

print(ray_dog.count('Chow-Chow'))  # count = 1





