"""
Functions
    -   Functions are small parts of code that realize specifics tasks
    -   Can or not has parameters
    -   Can execute similar process many times
OBS: If you write simple functions to simplify the code


"""
colors = ['green', 'yellow', 'blue', 'white']

# Integrate functions at Python Built-in
print(colors)  # ['green', 'yellow', 'blue', 'white']

course = 'Essential Python Program'
print(course)  # Essential Python Program

colors.append('purple')
print(colors)  # ['green', 'yellow', 'blue', 'white', 'purple']

colors.clear()
print(colors)  # []

print(help(print))  # None

# DRY - Don't Repeat Yourself
"""
# Function Definition

def function_name(input_parameters):
    function_block
    
Function => Snake Case and underline
input_parameters => separate with comma
function_block => function happens
"""


# Sample 1
def function_name():
    print('function')  # function


"""
1 - We can use other function inside
2 - Execute one task
3 - Not get input parameters
4 - Not return
"""

# Using function

# execute function
function_name()

"""
ATTENTION
Never forget parentheses

Sample:
# CORRECT
function()
# WRONG
function ()
function
"""


# Sample 2
def happy_birthday():
    print('Happy Birthday to you')
    print('Happy Birthday to you')


# for n in range(5):
#     happy_birthday()

# Create the variable with same type then the function

sing = happy_birthday
sing()
