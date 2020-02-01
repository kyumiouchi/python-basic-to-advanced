"""
String IO

Attention: to read or write files
    - read permission
    - write permission

StringIO -> read and create file in memory.
"""

from io import StringIO

message = "Normal String"

file = StringIO(message)
# file = open('file.txt', 'w')
print(file.read())  # Normal String
file.write(" Other text")

file.seek(0)

print(file.read())  # Normal String Other text

