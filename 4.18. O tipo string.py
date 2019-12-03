"""
String Type

In Python, the data is considered string type when:

- Single Quotation marks -> 'Yumi', '1234', 'True'
- Double quotation marks -> "Yumi", "1234", "True"
- Triple Single Quotation marks -> '''Yumi''', '''1234''', '''True'''
- Triple Double quotation marks -> " " "Yumi" " ", "" "12345" "", "" "True" ""(without space)

name = "Angelina \" Jolie"

name = '''Angelina
Jolie'''
name = "" "Angelina
Jolie" ""
name = 'Geek University'
name = "Ginas's Bar" -> Gina's Bar
name = 'Angelina \n Jolie'
print(name)
print(type(name))
name = 'Geek University'
print(name.lower()) -> geek university
print(name.split()) -> ['Geek', 'University']
print(name.upper()) -> GEEK UNIVERSITY

# [ 0,   1,   2,   3,   4,   5,   6,   7  , 8,   9 ,  10,  11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
name = 'Geek University'
print(name[0:4])  # Slice of string -> Geek

print(name[5:15])  # -> University

# [0, 1]
# ['Geek', 'University']
print(name.split())
print(name.split()[0])  # -> Geek
print(name.split()[1])  # -> University

"""
name = 'Geek University'
"""
[::-1] -> It started at first element until the last element and reverse
"""
print(name[::-1])  # -> ytisrevinU keeG
print(name[0:15], name[:15], name[0:], name[::])  # -> Geek University Geek University Geek University Geek University
print(name.replace('G', 'P'))  # -> Peek University
print(name.replace('e', 'i'))  # -> Giik Univirsity

name = 'ana'
print(name[::-1])  # palindrome -> ana
