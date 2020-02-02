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
"""
import os

# Directory
# os.rename('templates2', 'yumi2')
# OBS: If not exists, FIleNotFoundError

# OBS: If directory is not empty, OSError

# Files
os.rename('yumi2/z/teste.py', 'test_yumi.py')


