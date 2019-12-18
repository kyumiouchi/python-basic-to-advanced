"""
Collections -  Default Dict

When you create a Default dictionary you inform by default Dict. Inform value default just using lambda.
If access a not exist key, this key will be created and the default value is signed.

dictionary = {'course': 'Python Essential'}
print(dictionary)

print(dictionary['course'])
# print(dictionary['other'])  # KeyError: 'other'
"""

from collections import defaultdict

dictionary = defaultdict(lambda: 0)  # default value = 0 if not exist
print(dictionary)  # defaultdict(<function <lambda> at 0x00000215C55C6268>, {})

dictionary['course'] = 'Python Essential'

print(dictionary)  # defaultdict(<function <lambda> at 0x0000024FB5276268>, {'course': 'Python Essential'})
print(dictionary['other'])  # 0
print(dictionary)  # defaultdict(<function <lambda> at 0x0000024FB5276268>, {'course': 'Python Essential', 'other': 0})

