"""
Try, Except, Else and Finally

Example:
    - All input mus be treat Exception
"""

# Else -> Execute if not error happens

# number = 0
# try:
#     number = int(input('Write the code:'))
# except ValueError:
#     print(f'Value error')
# else:
#     print(f'You taped {number}')

# Finally -> close or move resources

number = 0
try:
    number = int(input('Write the code:'))
except ValueError:
    print(f'Value error')
else:
    print(f'You taped {number}')
finally:
    print('Execute finally')


# Complete sample5

#
# def divider(a, b):
#     try:
#         return int(a) / int(b)
#     except ValueError:
#         return 'Value error'
#     except ZeroDivisionError:
#         return 'Divider of zero'
#     except:
#         return 'Unknown error'
#
#
# num1 = input('First number: ')
# num2 = input('Second number: ')
#
# print(divider(num1, num2))
