"""
Dictionary

OBS: dictionary in other languages are knowledge as a map

Dictionary are collection with key and value type

Dictionary are represented as keys {}

print(type({}))  # <class 'dict'>

OBS: About dictionaries
    - Key and value are separated by two dots 'key':'value'
    - key and vale can be any type
    - you can miss data type
# Create dictionary
# Way 1
countries = {'br': 'Brazil', 'eua': 'United States', 'py': 'Paraguay'}

print(countries)  # {'br': 'Brazil', 'eua': 'United States', 'py': 'Paraguay'}
print(type(countries))  # <class 'dict'>

# Way 2 (less common)
countries = dict(br='Brazil', eua='United States', py='Paraguay')

print(countries)  # {'br': 'Brazil', 'eua': 'United States', 'py': 'Paraguay'}
print(type(countries))  # <class 'dict'>

# access elements
# Way 1 - access like tuple/list

print(countries['br'])  # Brazil
# print(countries['ru'])  # KeyError: 'ru'

# Way 2 - Access by get (RECOMMEND)
print(countries.get('br'))  # Brazil
print(countries.get('ru'))  # None


# Get not found the value 'None' and not print 'error'

russia = countries.get('ru')
if russia:  # i do not found country
    print('found country')
else:
    print('i do not found country')

country = countries.get('py')
if country:  # found country
    print('found country')
else:
    print('i do not found country')

# Standard if not found the key
russia = countries.get('ru', 'not found country')
print(russia)  # not found country

paraguay = countries.get('py', 'not found country')
print(paraguay)  # Paraguay
countries = {'br': 'Brazil', 'eua': 'United States', 'py': 'Paraguay'}
print('br' in countries)  # True
print('ru' in countries)  # False
print('United States' in countries)  # False

if 'ru' in countries:
    russia = countries['ru']

# Any ind of type float, int, string, boolean.. include tuple, dictionary, as key
# Tuple is interesting because dictionary key is unchanging.
location = {
    (10.0000, 10.3000): 'Tokyo office',
    (43.4325, 66.5464): 'New York office',
    (98.9898, 56.4322): 'Sao Paulo office'
}

print(location)  # {(10.0, 10.3): 'Tokyo office', (43.4325, 66.5464): 'New York office', (98.9898, 56.4322): 'Sao
# Paulo office'}
print(type(location))  # <class 'dict'>

# Add elements at dictionary
values = {'jan': 100, 'fev': 100, 'mar': 100}
print(values)  # {'jan': 100, 'fev': 100, 'mar': 100}
print(type(values))  # <class 'dict'>

# Way 1
values['apr'] = 350  # {'jan': 100, 'fev': 100, 'mar': 100, 'apr': 350}
print(values)

# Way 2
new_month = {'may': 500}
values.update(new_month)  # {'jan': 100, 'fev': 100, 'mar': 100, 'apr': 350, 'may': 500}
print(values)

# Way 2.1
values.update({'jun': 700})  # {'jan': 100, 'fev': 100, 'mar': 100, 'apr': 350, 'may': 500, 'jun': 700}
print(values)

# Update data at dictionary [add or update data at dictionary is the same].
# Dictionary does not have repeated key.
values['apr'] = 600  # {'jan': 100, 'fev': 100, 'mar': 100, 'apr': 600, 'may': 500, 'jun': 700}
print(values)
values.update({'jun': 1000})  # {'jan': 100, 'fev': 100, 'mar': 100, 'apr': 600, 'may': 500, 'jun': 1000}
print(values)


# Remove item

# Way 1
removed = values.pop('jan')
# inform the key or KeyError shows
print(removed, values)  # 100 {'fev': 100, 'mar': 100, 'apr': 600, 'may': 500, 'jun': 1000}
# Way 2 -> do not return value -> KeyError shows
del values['fev']
print(values)  # {'mar': 100, 'apr': 600, 'may': 500, 'jun': 1000}

# 1 - list to save data at store

car = []

product1 = ['Playstation 4', 1, 2300.00]
product2 = ['God Of War', 1, 150.00]

car.append(product1)
car.append(product2)

print(car)  [['Playstation 4', 1, 2300.0], ['God Of War', 1, 150.0]]

# 2 - Tuple
product1 = ('Playstation 4', 1, 2300.00)
product2 = ('God Of War', 1, 150.00)

car = (product1, product2)
print(car)  # (('Playstation 4', 1, 2300.0), ('God Of War', 1, 150.0))

# dictionary

car = []

product1 = {'name': 'Playstation 4', 'quantity': 1, 'price': 2300.00}
product2 = {'name': 'God Of War', 'quantity': 1, 'price': 150.00}

car.append(product1)
car.append(product2)
print(car)  # [{'name': 'Playstation 4', 'quantity': 1, 'price': 2300.0}, {'name': 'God Of War', 'quantity': 1,
# 'price': 150.0}]

# Clear dictionary
dictionary.clear()
print(dictionary)  # (Empty)

# Dictionary Method
dictionary = dict(a=1, b=2, c=3)
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}
print(type(dictionary))  # <class 'dict'>

# Copy dictionary to another
# Way 1 => Deep Copy
new_dictionary = dictionary.copy()
print(new_dictionary)  # {'a': 1, 'b': 2, 'c': 3}

new_dictionary['d'] = 4
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}
print(new_dictionary)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Way 1 => Shallow Copy
new_dictionary = dictionary
print(new_dictionary)  # {'a': 1, 'b': 2, 'c': 3}

new_dictionary['d'] = 4
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(new_dictionary)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
"""

# Not usual create dictionary
other = {}.fromkeys('a', 'b')

print(other)
print(type(other))

other = {}.fromkeys(['name', 'score', 'email', 'profile'], 'unknowledge')

print(other)  # {'name': 'unknowledge', 'score': 'unknowledge', 'email': 'unknowledge', 'profile': 'unknowledge'}
print(type(other))  # <class 'dict'>

# Dictionary not repeat
other = {}.fromkeys('tests', 'value')

print(other)  # {'t': 'value', 'e': 'value', 's': 'value'}

other = {}.fromkeys(range(1, 11), 'value')

print(other)  # {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value', 8: 'value',
# 9: 'value', 10: 'value'}


















