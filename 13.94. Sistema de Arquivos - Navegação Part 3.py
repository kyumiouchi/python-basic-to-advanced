"""


import sys
import os
print(sys.platform)  # win32

print(os.getcwd())
result = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(result)

print(os.getcwd())
"""
import os

# list the directory
print(os.listdir())
print(len(os.listdir()))

# print(os.listdir('etc'))
scanner = os.scandir('.git')
# print(scanner)  # <nt.ScandirIterator object at 0x0000011C3C885900>
# print(list(scanner))  # [<DirEntry 'COMMIT_EDITMSG'>, <DirEntry 'config'>, <DirEntry 'description'>, <DirEntry 'FETCH_HEAD'>, <DirEntry 'HEAD'>, <DirEntry 'hooks'>, <DirEntry 'index'>, <DirEntry 'info'>, <DirEntry 'logs'>, <DirEntry 'objects'>, <DirEntry 'ORIG_HEAD'>, <DirEntry 'packed-refs'>, <DirEntry 'refs'>, <DirEntry 'smartgit'>, <DirEntry 'smartgit.config'>]

files = list(scanner)
print(files)  # [<DirEntry 'COMMIT_EDITMSG'>, <DirEntry 'config'>, <DirEntry 'description'>, <DirEntry 'FETCH_HEAD'>, <DirEntry 'HEAD'>, <DirEntry 'hooks'>, <DirEntry 'index'>, <DirEntry 'info'>, <DirEntry 'logs'>, <DirEntry 'objects'>, <DirEntry 'ORIG_HEAD'>, <DirEntry 'packed-refs'>, <DirEntry 'refs'>, <DirEntry 'smartgit'>, <DirEntry 'smartgit.config'>]
print(dir(files[0]))  # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__fspath__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'inode', 'is_dir', 'is_file', 'is_symlink', 'name', 'path', 'stat']

print(files[0].inode())  # 6473924464362657
print(files[0].is_dir())  # False
print(files[0].is_file())  # True
print(files[0].is_symlink())  # False
print(files[0].name)  # COMMIT_EDITMSG
print(files[0].path)  # .git\COMMIT_EDITMSG
print(files[0].stat())  # os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=17, st_atime=1580588828, st_mtime=1580588828, st_ctime=1578868332)

#OBS: close scandir() is mandatory
scanner.close()
