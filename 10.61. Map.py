"""
Map
With map we map the value to funtion
"""
import math

def area(r):
    # Calculate area
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

rays = [2, 5, 7.1, 0.3, 10, 44]

# Ordinary Way
areas =[]
for r in rays:
    areas.append(area(r))

print(areas)

# Way 2 - Map
# Maps is a function that gets two parameters: First a function and the second a iteration
areas = map(area, rays)

print(areas)  # <map object at 0x000001B8699C2F60>
print(type(areas))  # <class 'map'>
print(list(areas))  # [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814,
# 314.1592653589793, 6082.12337734984]

# way 3 - Map + lambda
print(set(map(lambda result: math.pi * (result ** 2), rays)))

# OBS: after use the result, this variable is empty

# To fix - Map
# Has iteration data:
# data: a1, a2, ..., an
# Has a function: Function : f(x)
# Maps will map each element and apply the function
# Object Map: f(a1), f(a2), f(a3),..., f(an)

countries = [('Berlim', 29), ('Cairo', 36), ('Los Angeles', 26)]
print(countries)
# [('Berlim', 29), ('Cairo', 36), ('Los Angeles', 26)]

# f = 9/5 * c +32
# Lambda
c_to_f = lambda  data: (data[0], (9/5) * data[1] + 32)
print(list(map(c_to_f, countries)))
# [('Berlim', 84.2), ('Cairo', 96.8), ('Los Angeles', 78.80000000000001)]





















