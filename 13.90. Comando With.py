"""
Block With


Steps working with files:
# 1 - open file
# 2 - Manipulation file
# 3 - Close file
"""


with open('text.txt') as file:
    print(file.readlines())
    print(file.closed())

# print(file.read())
print(file.closed)