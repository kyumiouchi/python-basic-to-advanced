"""
*args understanding

    -   args is a parameter. Can be anything if start with *
*xis

Community chose *args

Whats is *args?
args is pass as parameter at function, Value extra as tuple

# Samples Wrong
def sum_all_value(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4


print(sum_all_value(4, 6, 9))  # 23
def sum_all_value(name, email, *args):
    return sum(args)


print(sum_all_value('name', 'Ouchi'))
print(sum_all_value('name', 'Ouchi', 1))
print(sum_all_value('name', 'Ouchi', 1, 2))
print(sum_all_value('name', 'Ouchi', 1, 2, 3))
print(sum_all_value('name', 'Ouchi', 1, 2, 3, 4))

print(sum_all_value('name', 'Ouchi', 1.1, 2.34, 3, 4))

def verify_info(*args):
    if 'Yumi' in args and 'Ouchi' in args:
        return 'Welcome Yumi'
    return 'I do not know who you are'

print(verify_info())
print(verify_info(1, True, 'Ouchi', 'Yumi'))
print(verify_info(1, True, 234234, 'Yumi'))
"""


def sum_all_value(*args):
    return sum(args)


print(sum_all_value())  # 0
print(sum_all_value(1))  # 1

numbers = (1, 2, 3, 4, 5, 6)
# print(sum_all_value(numbers))  # TypeError: unsupported operand type(s) for +: 'int' and 'list'

# Unpacked
print(sum_all_value(*numbers))
# * collection of data and unpacked the data

numbers = [1, 2, 3, 4, 5, 6]
print(sum_all_value(*numbers))
