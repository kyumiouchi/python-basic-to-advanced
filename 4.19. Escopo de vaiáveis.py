"""
Scope of Variables
Two cases of scope

1- Global variables:
    - Global Variables are recognized, in other words, understand your scope in all program
2- Local variables:
    - Local variables are knowledge as a bloc where was declared, where you scope is limited in your bloc
    where was declared

Declared Variable in Python:

variable_name = variable_value

Python is a dynamic type language. This means that the variable declared not necessarily input the variable type.
The language infers the attribute.

Sample in C/ Java:
int number = 42;
"""

number = 2  # reassignment / global variable
print(number)
print(type(number))

new = 0
if number > 10:
    new = number + 10  # local variable
    print(new)
print(new)  # if is local -> NameError: name 'new' is not defined and number < 10, is global -> new = 0


