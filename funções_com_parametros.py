"""
Functions with parameters

    -   Functions processed and receive data

input -> processing > output

Function type:
    - No input
    - No output
    - input, but no output
    - no input with output
    - input and output


def quad(number):
    return number * number


print(quad(4))  # 16

return_value = quad(40)
print(return_value)  # 1600
print(quad())  # TypeError: quad() missing 1 required positional argument: 'number'

def happy_birthday(person):
    print('Happy birthday to you')
    print(f'Happy birthday to {person}')

happy_birthday('Patricia')  # Happy birthday to Patricia


def sum(a, b):
    return a + b


def multiply(num1, num2):
    return num1 + num2


def other(num1, b, msg):
    return (num1 + b) * msg


print(sum(2, 5))  # 7
print(sum(67, 5))  # 72

print(multiply(2, 5))  # 7
print(multiply(76, 5))  # 81

print(other(2, 5, 'Geek'))  # GeekGeekGeekGeekGeekGeekGeek
print(other(2, 5, 'Yumi'))  # YumiYumiYumiYumiYumiYumiYumi

# TypeError with input incorrect
# print(sum(2))  # TypeError: sum() missing 1 required positional argument: 'b'
# print(sum(2, 5, 5))  # TypeError: sum() takes 2 positional arguments but 3 were given


def complete_name(name, surname):  # parameter
    return f'Complete name is {name} {surname}'


print(complete_name('Angelina', 'Jolie'))  # arguments

# sort important
print(complete_name('Jolie', 'Angelina'))  # arguments
print(complete_name(surname='Jolie', name='Angelina'))  # Complete name is Angelina Jolie
print(complete_name(name='Jolie', surname='Angelina'))  # Complete name is Jolie Angelina

"""


def odd_sum(number):
    total = 0
    for num in number:
        if num % 2 != 0:
            total = total + num
    return total

if __name__ == '__main__':
    list_value = [1, 2, 3, 4, 5, 6, 7]

    print(odd_sum(list_value))  # 16

    tuple_value = 1, 2, 3, 4, 5, 6, 7
    print(odd_sum(tuple_value))  # 16
# else:
#     print('The function module was imported')
