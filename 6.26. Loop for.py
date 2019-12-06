"""
Loop for

Loop -> Repetition Structure
For -> One of that structure

C or Java

for (int i = 0; i < 10; i++){
    // loop execution
}

Python
for item in iteration:
    //loop execute

Works with sequence and iterative value
    - String
        name = 'Geek University'
    - List
        list = [1,2,3,4]
    - Range
        number = range(1, 10)

name = 'Geek University'
list_number = [10, 20, 30, 40]
number = range(1, 10)  # list transform


# Sample 1 - string iteration
for letter in name:
    print(letter)

# Sample 2 - list iteration
for num in list_number:
    print(num)

# Sample 2 - range
# the value 10 is not included
# 1,2,3,4,5,6,7,8,9,10 (Not included - 10)
for num in number:
    print(num)

print(name[0:5])
print(name[0:14])
print(name[0:15])
print(name[0:1000])

Enumerate:
((0, 'Y'), (1, 'u'), (2, 'm'), (3, 'i'))
for index, letter in enumerate(name):
    print("i:", index, "v:", letter, "name[i]:",  name[index])

for _, v in enumerate(name):
    print("v:", v)

for value in enumerate(name):
    print("v:", value)

qtd = int(input('Quantity of iterations at loop?  '))
sum_value = 0

for n in range(1, qtd+1):
    num = int(input(f'Inform the value of {n}/{qtd}:  '))
    sum_value = sum_value + num
print(f'Sum is {sum_value}')

name = 'Geek University'
for letter in name:
    print(letter, end='')  # Geek University

# print(help(print))  # print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
name = 'Geek University'
print(name * 3)  # 3 times-> Geek UniversityGeek UniversityGeek University
"""
# Original: U+1F60D
# Modification: U0001F60D

# emoji = '\U0001F60D' # 😍😍😍😍😍😍😍😍😍😍

# Original: U+1F605
# Modification: U0001F605

emoji = '\U0001F605'  # 😅😅😅😅😅😅😅😅😅😅
for _ in range(3):
    for num in range(1, 11):
        print(f'{emoji * num}')
