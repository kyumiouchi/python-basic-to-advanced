"""
Logic structure: and, or not, is

Unary operators:
    - not
Binary operators:
    - and, or, is
AND - both have to be True
OR - one of than have to be True
NOT - boolean invert (True = False, False = True)
IS - compare with the second item
"""
available = True
online = True

# Correct at Python way
if not available:  # Welcome User
    print('You need to activate you account. Please, check your e-mail!')
else:
    print('Welcome User')

if available and online:  # Welcome User
    print('Welcome User')
else:
    print('You need to activate you account. Please, check your e-mail!')

print(not True)  # False
print(not False)  # True

# Wrong at Python way
if available is False:  # Welcome User
    print('You need to activate you account. Please, check your e-mail!')
else:
    print('Welcome User')

name = 'Geek'
print(name.isupper())  # False

print(name.istitle())  # True

print(1 == 1)  # True
print(1 is 1)  # True
print(name is 'Geek')  # True
print(name is 'geek')  # False






