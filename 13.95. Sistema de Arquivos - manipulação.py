"""
File system - Manipulation

import os

# file
print(os.path.exists('file.txt'))  # False
print(os.path.exists('first.py'))  # True
# relative directory
print(os.path.exists('test_yumi'))  # True
print(os.path.exists('test_yumi/test_yumi2'))  # True
print(os.path.exists('other'))  # False

# absolute directory
print(os.path.exists('Y:/Study/Python-basico-avancado/test_yumi'))  # True
print(os.path.exists('Y:/Study/Python-basico-avancado/first.py'))  # True


# Way 1
open('file-test.txt', 'w').close()

# Way 2
open('file-test2.txt', 'a').close()

# Way 3
with open('file-test3.txt', 'w') as file:
    pass


# Create one by one
# os.mknod('file-test4.txt')
# os.mknod('Y:/Study/Python-basico-avancado/file/file-test5.txt')

# OBS1: Admin permission to work
# OBS2: error FileExistsError when exists

# relative
os.mkdir('templates')
# absolute
os.mkdir('Y:/Study/Python-basico-avancado/templates')

# OBS: if exist, FileExistsError
# OBS: If do not has permission, PermissionError

# Create multi directories
os.makedirs('Y:/Study/Python-basico-avancado/templates2/z')

# OBS: If exists, FileExistsError

os.makedirs('Y:/Study/Python-basico-avancado/templates2/z', exist_ok=True)
# No Error exception to create

# Directory
# os.rename('templates2', 'yumi2')
# OBS: If not exists, FIleNotFoundError

# OBS: If directory is not empty, OSError

# Files
os.rename('text.txt', 'text2.py')

# Attention: When you delete file/folder, those desappear and does not go to trash.
os.remove('geek.txt')

# OBS: if the file is using then error.
# OBS: if not exist FileNotFoundError: [Errno 2] No such file or directory: 'geek.txt'

# os.remove('yumi2')
# OBS: Just remove file. IsADirectoryError: [Errno 21] Is a directory: 'yumi2'

os.rmdir('yumi2/z/k')
# OBS: if directory is not empty. OSError: [Errno 39] Directory not empty: 'yumi2/z'
# OBS: if not directory not exist. FileNotFoundError: [Errno 2] No such file or directory: 'yumi2/z/k'

for file in os.scandir('yumi2/z'):
    if file.is_file():
        os.remove(file.path)
    else:
        os.rmdir(file.path)

os.removedirs('yumi2/z/a/b')
# remove yumi2/z/a/b directories

conda install send2trash

from send2trash import send2trash
os.remove('test_yumi.py')  # delete immediately

send2trash('text2.py')  # go to trash

# CREATE DIRECTORY TEMPORARY
# Work with temporary director
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Tmeporary file {tmp}')
    with open(os.path.join(tmp, 'temp_file.txt'), 'w') as file:
        file.write('Yumi Ouchi\n')
    input()

# create directory 'tmp', open the same and create a text. At the end, use the input() to keep the file alive.


# Create file temporary

with tempfile.TemporaryDirectory() as tmp:
    tmp.write(b'Yumi Ouchi\n')
    tmp.seek(0)
    print(tmp.read())

file = tempfile.TemporaryDirectory()
file.write(b'Yumi Ouchi\n')
file.seek(0)
print(file.read())
file.close()


file = tempfile.NamedTemporaryFile()
file.write(b'Yumi Ouchi\n')
print(file.name)
print(file.read())
input()
file.close()
"""
import tempfile


