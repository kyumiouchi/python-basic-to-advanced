"""
Day 4 - 30/11
Float Type -> real type or decimal -> Used when we need accurate

Decimal places

OBS: Separate of decimal places are dot and not comma
"""

# Wrong -> Float standpoint
value = 1, 44
print(value)
print(type(value))

# Correct -> Flow standpoint
value = 1.44
print(value)
print(type(value))

# Possible
value1, value2 = 1, 44
print(value1)
print(type(value1))
print(value2)
print(type(value2))

# We can convert float type to int type
"""
OBS: To convert float type to integer type we lost the accurate
"""
result = int(value)
print(result)
print(type(result))
print(float(result))

# We can use complex number
num_complex = 5j
print(num_complex)
print(type(num_complex))

print(num_complex ** 2)

salary_he = 2.56
salary_she = 3.67
total_float = salary_he + salary_she
print(total_float)
total_int = int(salary_he) + int(salary_she)
print(total_int)
print(dir(salary_she))
