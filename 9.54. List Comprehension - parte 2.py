"""
List Comprehension - Part 2

We can add conditional structure to out list Comprehension

"""

# Sample

# 1
numbers = [1, 2, 3, 4, 5]

even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 != 0]

print(even)  # [2, 4]
print(odd)  # [1, 3, 5]

# Refactor

# Any number even is 0 and 0 in Python means False. not False = True
even = [number for number in numbers if not number % 2]
odd = [number for number in numbers if number % 2]

print(even)  # [2, 4]
print(odd)  # [1, 3, 5]


# 2
result = [number * 2 if number % 2 == 0 else number / 2 for number in numbers]
print(result)  # [0.5, 4, 1.5, 8, 2.5]

result = [number + 2 if not number % 2 else number - 1 for number in numbers]
print(result)  # [0, 4, 2, 6, 4]
