"""
Bool type

bool algebra, created by George Boole

2 constants, True and False

True and False

Obs: Start with uppercase

Wrong;

true, false

Correct:

True, False
"""

activated = False
print(activated)

"""
basic operations
"""

# Negative (not)

"""
If you do the negation of False of bool the result is True and the True of bool the result is False
"""

print(not activated)

# OR (or)
"""
Binary operation -  one of the value must be True
"""
print(True or False)  # -> True
print(False or True)  # -> True
print(True or True)  # -> True
print(False or False)  # -> False

# AND (and)
"""
Binary operation -  both are True to be True
"""
print(True or False)  # -> False
print(False or True)  # -> False
print(True or True)  # -> True
print(False or False)  # -> False

print(5 > 6)  # -> False
print(5 < 6)  # -> True
print(6 == 6)  # -> True
print(4 <= 6)  # -> True

num1 = 7
num2 = 8

print(num1 < num2)  # -> True
print(num1 == num2)  # -> False
print(num1 < num2 or num1 > 3)  # -> True
print(num1 < num2 and num1 > 3)  # -> True

print(type(False))  # -> <class 'bool'>
print(type(True))  # -> <class 'bool'>

print(type(activated))  # -> <class 'bool'>

print(dir(activated))  # -> ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__',
# '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__',
# '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__',
# '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
# '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__',
# '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
# '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes',
# 'imag', 'numerator', 'real', 'to_bytes']











