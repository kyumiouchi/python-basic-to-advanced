"""
Packages

Module -> many functions

Package -> many collection of modules

OBS: Python 2.X needs __init__.py, Python 3.X not obligation


from test_yumi import yumi1, yumi2
from test_yumi.test_yumi2 import yumi3, yumi4

print(yumi1.function1(4, 5))  # 9

print(yumi2.course)  # Python program
print(yumi2.function2())  # Python program
print(yumi3.function3())  # Yumi
print(yumi4.function4())  # Ouchi
"""

from test_yumi.yumi1 import function1
from test_yumi.test_yumi2.yumi4 import function4

print(function1(4, 7))  # 11
print(function4())  # Ouchi
