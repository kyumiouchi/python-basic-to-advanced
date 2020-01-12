"""
Seek and Cursors

seek() -> move cursor around the file
file = open('text.txt')
print(file.read())

# Moving cursor with seek() function
# seek() -> receive the parameter where the cursor can be

file.seek(0)  # position 0
print(file.read())

file.seek(20)  # position 20
print(file.read())

# Read line to line -> readline()
file = open('text.txt')
# print(file.readline())
# print(file.readline())
read_file = file.readline()
print(type(read_file))
print(read_file)
print(read_file.split(' '))

# read lines
file = open('text.txt')
file_read = file.readline()
print(len(file_read))  # 32

# OBS: When open file with open() function. This creates a connection with computer disk and this program. This call
# as STREAMING. And in the end it is necessary close the connection with close() function
# 1- Open file
file = open('text.txt')
# 2- Work with file
print(file.read())

print(file.closed)  # if is closed FALSE and open TRUE # False
# 3- CLose file
file.close()
print(file.closed)  # True
# print(file.read())  # ValueError: I/O operation on closed file.
# OBS: To manipulation the file after close shows the error ValueError
# OBS: Close to say the SO that you are not using the file anymore
"""

file = open('text.txt')

# read() -> Can limited the quantity od characters
print(file.read(50))  # Read 50 characters
