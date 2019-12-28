"""
Understanding ***Kwargs

We can call ** xis, but by convention call by **kwargs

On more parameters, *args is tuple, and *kwargs is named parameters as dictionary


# Sample 1
def favorite_color(**kwargs):
    print(kwargs)

favorite_color(yumi='blue', luciana='bçack', adriana='white', luiz='pink')
# {'yumi': 'blue', 'luciana': 'bçack', 'adriana': 'white', 'luiz': 'pink'}

# Sample 2
def favorite_color(**kwargs):
    for person, color in kwargs.items():
        print(person, color, end=', ')


# OBS: *args and *kwargs not obligation
favorite_color()  # (empty)
favorite_color(yumi='intelligent')
# yumi intelligent,

favorite_color(yumi='blue', luciana='bçack', adriana='white', luiz='pink')
# yumi blue, luciana bçack, adriana white, luiz pink,

def special_agreement(**kwargs):
    if 'yumi' in kwargs and kwargs['yumi'] == 'Python':
        return 'You receive agreement Yumi'
    elif 'yumi' in kwargs:
        return f"{kwargs['yumi']} Geek"
    return 'How are you?'

print(special_agreement())  # How are you?
print(special_agreement(yumi='Python'))  # You receive agreement
print(special_agreement(yumi='Hello'))  # Hello Geek
print(special_agreement(yumi='special'))  # special Geek

# OBS: SORT:
    - Obligation Parameters
    - *args
    - Default Parameters
    - **kwargs
"""


def my_function(age, name, *args, single=False, **kwargs):
    print(f"Obligation: {name} is {age} years old", end='; ')
    print("Args:", args, end='; ')
    if single:
        print("Default:", 'Single', end='; ')
    else:
        print("Default:", 'Married', end='; ')
    print("Kwargs:", kwargs)


my_function(30, 'Yumi')
# Obligation: Yumi is 30 years old; Args: (); Default: Married; Kwargs: {}
my_function(29, 'Luciana', 4, 5, 6, single=True)
# Obligation: Luciana is 29 years old; Args: (4, 5, 6); Default: Single; Kwargs: {}
my_function(34, 'Luiz', eu='Not', you='Go')
# Obligation: Luiz is 34 years old; Args: (); Default: Married; Kwargs: {'eu': 'Not', 'you': 'Go'}
my_function(21, 'Carlla', 10, 5, 3, java=False, python=True, single=True)
# Obligation: Carlla is 21 years old; Args: (10, 5, 3); Default: Single; Kwargs: {'java': False, 'python': True}
