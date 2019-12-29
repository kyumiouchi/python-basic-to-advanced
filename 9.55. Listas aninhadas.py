"""
Nested lists

- Data structure call as arrays
    - one-dimensional ( arrays/ Vectors)
    - two-dimensional (Matrices)

In Python, as Nested Lists

"""
# Samples
list_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrices 3x3
print(list_numbers)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(list_numbers))  # <class 'list'>

# How to access the data?
print(list_numbers[0])  # [1, 2, 3]
print(list_numbers[0][1])  # 2
print(list_numbers[2][2])  # 9
print(list_numbers[2][-1])  # 9
print(list_numbers[2][-2])  # 8

# Iteration with loop in the nested list

for list_item in list_numbers:
    for number in list_item:
        print(number, end=', ')
# 1, 2, 3, 4, 5, 6, 7, 8, 9,
print()
# List Comprehension
result = [[print(number, end=', ') for number in list_item] for list_item in list_numbers]
# 1, 2, 3, 4, 5, 6, 7, 8, 9,

print()
# Generate matrix 3x3
matrix3x3 = [[number for number in range(1, 4)] for value in range(1, 4)]
print(matrix3x3)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

tic_tac_toe = [['X' if number % 2 == 0 else '0' for number in range(1, 4)] for value in range(1, 4)]
print(tic_tac_toe)  # [['0', 'X', '0'], ['0', 'X', '0'], ['0', 'X', '0']]

asterisk = [['*' for i in range(1, 4)] for j in range(1, 4)]
print(asterisk)  # [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
