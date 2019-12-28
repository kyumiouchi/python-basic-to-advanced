"""
Docstring functions

__doc__ => access the special docstring


# print(help(print))  # print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

def hello():
    "" " Simple function to say Hello" ""
    return 'Hello'


print(hello())

print(help(hello()))

print(hello.__doc__)  # Simple function to say Hello
"""


def exponential(number, potential=2):
    """
    Return quad of number or the potentia of numbers
    :param number: Number to generate the exponential
    :param potential: Potential => 2 si the standard
    :return: result of number and potential
    """
    return number ** potential


print(help(exponential))
# exponential(number, potential=2)
#     Return quad of number or the potentia of numbers
#     :param number: Number to generate the exponential
#     :param potential: Potential => 2 si the standard
#     :return: result of number and potential

print(exponential.__doc__)  # Simple function to say Hello
    # Return quad of number or the potentia of numbers
    # :param number: Number to generate the exponential
    # :param potential: Potential => 2 si the standard
    # :return: result of number and potential