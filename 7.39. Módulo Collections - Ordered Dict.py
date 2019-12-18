"""
Collections; Ordered Dict
"""

from collections import OrderedDict
# Order of insertion is not guaranteed
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key, value in dictionary.items():
    print(f'key={key}:value={value}')


dictionary_ordered = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for key, value in dictionary_ordered.items():
    print(f'key={key}:value={value}')

# Difference between OrderedDict and Dict

# Dict
dictionary1 = {'a': 1, 'b': 2}
dictionary2 = {'b': 2, 'a': 1}

print(dictionary1 == dictionary2)  # True => Order is not important

# Ordered Dict
ordered_dictionary1 = OrderedDict({'a': 1, 'b': 2})
ordered_dictionary2 = OrderedDict({'b': 2, 'a': 1})

print(ordered_dictionary1 == ordered_dictionary2)  # False => Order is important

