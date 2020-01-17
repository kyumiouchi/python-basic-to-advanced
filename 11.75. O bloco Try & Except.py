"""
Try/Except

We use the try/except block to treat errors at code.

try:
    // problem execute
execute:
    // what to do if show this error

# Sample 1 - Error generic
try:
    geek()
except:
    print('Some problem happens')
# Some problem happens

# Try execute geek(), if error happens, print error message.

# Sample 2 - Error generic
try:
    geek()
except:
    print('Some problem happens')
# Some problem happens
# Treat error with generic way it is not a good way. It is better to be specific.

# Sample 3 - Error generic
try:
    geek()
except NameError:
    print('Function not exist function')
# Function not exist function

# Sample 4 - Error generic
try:
    len(5)
except TypeError as err:
    print(f'The app created the error as follow: {err}')
# The app created the error as follow: object of type 'int' has no len()

try:
    # len(5)
    geek()
except NameError as err:
    print(f'NameError: {err}')
except TypeError as err:
    print(f'TypeError: {err}')
except:
    print('Different Error')
"""

def take_value(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None
    except TypeError:
        return None

dict = {"name": "Geek"}

print(take_value(7, "name"))


