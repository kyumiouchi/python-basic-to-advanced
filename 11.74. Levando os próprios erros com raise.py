"""
Using Raise

raise -> Show exception

OBS: raise is not a function.

Raise is useful to create our exception and message of error.

In general, the way is:

raise TypeOfError('Message of Error')

# raise ValueError('Incorrect value')

def color(text, color):
    if type(text) is not str:
        raise TypeError('text must be a STRING type')
    if type(color) is not str:
        raise TypeError('color must be a STRING type')
    print(f'The text{text} is {color} color')


color(True, 'blue')

OBS: Raise finish the function like RETURN


"""

# raise ValueError('Incorrect value')


def color(text, color):
    colors = ('green', 'yellow', 'blue', 'white')
    if type(text) is not str:
        raise TypeError('text must be a STRING type')
    if type(color) is not str:
        raise TypeError('color must be a STRING type')
    if color not in colors:
        raise ValueError(f'The color must be: {colors}')
    print(f'The text{text} is {color} color')


color('HUM', 'black')
