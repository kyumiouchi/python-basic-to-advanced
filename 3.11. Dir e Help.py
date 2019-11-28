"""
Python utilities to aid the program
Dir -> Show all the available attributes/properties and function/methods to determinate the variable and data type.

dir(data/variable type)

Help -> Show the documentation/who to use the available attributes/properties and functions/methods
to determinate variable and data type.

help(data type/variable property)
"""

print("Geek University")
print(dir("Geek"))
help("Geek".lower)
print("Geek".lower())
help("Geek".upper)
print("Geek".upper())
print("Geek".title())
print("yumi ouchi".title())
print("YUMI OUCHI".title())
# help(4.real)
num = 4
help(num.real)
print(num.real)
# num.to_bytes()
print(num.__add__(6))
print(num + 6)


