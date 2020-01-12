"""
Read file

open() -> open file. Use one parameter (file name). Return _io.TextIOWrapper. The standard is r - read
# If not found file as show the FileNotFoundError

# place : https://docs.python.org/3/library/functions.html#open
"""

file = open('text.txt')
# print(file)  # <_io.TextIOWrapper name='text.txt' mode='r' encoding='cp1252'>
# print(type(file))  # <class '_io.TextIOWrapper'>
# Read the content after open you have to use read() function
string_file = file.read()
print(type(string_file))
print(len(string_file))
print(string_file)  # read all content
print(file.read())  # Nothing happen


# OBS: Python uses cursor to read files.
