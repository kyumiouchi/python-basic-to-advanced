"""
Loop while

General form;

while bool_expression:
    //execute loop

Repeat until bool expression is True


bool expression is all expression where the result is True or False

Sample:

num = 5
num < 5 #  False
num > 5 #  False

# sample 1
number = 1
while number < 10:  # 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(number, end=", ")
    number = number + 1

# OBS Take care about stop criteria because can cause infinite loop

Java or C

while(expression){
    //execution
}

# do while (C or Java)

do {

} while(expression);
"""

# Sample 2

answer = ''

while answer != 'yes':
    answer = input('Did you finish Andrew? ')

