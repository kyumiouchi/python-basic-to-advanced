"""
Lambdas

AS known as expression lambda or lambdas. Function anonymous


# FUnction Python

def sum(a, b):
    return a + b

def function(x):
    return 3 * x + 1

print(function(4))  # 13
print(function(7))  # 22


# Expression lambda
lambda x: 3 * x + 1

# How can I use expression lambda?
calculation = lambda x: 3 * x + 1
print(calculation(4))  # 13
print(calculation(7))  # 22

# We can use expression lambda with multiply inputs90
complete_name = lambda name, surname: name.strip().title() + ' ' + surname.strip().title()
print(complete_name( 'angelina', 'JOLIE'))  # Angelina Jolie
print(complete_name( ' YUMI ', '  OUCHI '))  # Yumi Ouchi
love = lambda: 'How not love python'
one = lambda x: 3*x+1
two = lambda x, y: (x * y) ** 0.5
three = lambda x, y, z: x + y + z

print(love())  # print(love())
print(one(1))  # 4
print(two(2, 3))  # 2.449489742783178
print(three(2, 3, 4))  # 9

# Type error with more parameters

people = ['Lais Balbe', 'Danilo Crazy', 'Anielle Matos', 'Rafael Duda', 'Yumi Ouchi', 'Ada Victoria']
print(people)  # ['Lais Balbe', 'Danilo Crazy', 'Anielle Matos', 'Rafael Duda', 'Yumi Ouchi', 'Ada Victoria']

people.sort(key=lambda surname: surname.split(' ')[-1].lower())
print(people)  # ['Lais Balbe', 'Danilo Crazy', 'Rafael Duda', 'Anielle Matos', 'Yumi Ouchi', 'Ada Victoria']
"""
# Quad function
def quad_function(a, b, c):
        """ Return a * x ** 2 + b * x + c"""
        return lambda x:  a * x ** 2 + b * x + c

quadrad = quad_function(2, 3, -5)

print(quadrad(0))  # -5
print(quadrad(1))  # 0
print(quadrad(2))  # 9

print(quad_function(1, 2, 3)(2))  # 11



