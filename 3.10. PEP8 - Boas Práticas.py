"""
PEP 8 (Python Enhancement Proposals) -> Style Guide for python Code

-----------------------------------------------------------------------
import this -> The Zen of Python

The idea of PEP8 is to write the Python code of Python way
-----------------------------------------------------------------------

[1] Camel Case to the name of the classes;

class Calculator:
    pass
class ScientificCalculator:
    pass

[2] Lowercase, separate with underline function or variable names;

def function_name():
    pass
def function_name_another():
    pass
variable_name = 10

[3] Indentation before code has 4 space keys
if 'a' in 'banana':
    print('tem')

[4] White lines
    - Separate function and definition classes with 2 white lines
    - Methods inside classes must separate with 1 white line

[5] Imports
    - imports must be into separate lines

# Correct
import sys
import os
# Incorrect
import sys, os

# Recommendations - same package
from types import (
    SprintType,
    ListType,
    SetType,
    OtherType
)

[6] Space in expressions and instructions

# Don't do
1) function ( something[ 1 ], { other : 2 } )
2) dict ['key'] = list [index]
3)
x             = 1
y             = 2
long_variable = 3

# Do
1) function(something[1], {other: 2})
2) dict['key'] = list[index]
3)
x = 1
y = 2
long_variable = 3

[7] Finish instruction with a new line

"""

import this
