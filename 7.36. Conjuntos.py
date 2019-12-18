"""
Sets

Sets theory of mathematic

Same then mathematic
    - Sets can not duplicated value
    - Sets can not sort value
    - Not index -  no access by index
We need to save , but we do not import with sorted.

Difference between dictionary and Sets
    - Dictionary has key/ value
    - Set has value

# Sets defined:

# Way 1

set_value = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

print(set_value)  # {1, 2, 3, 4, 5, 6, 7}
print(type(set_value))  # <class 'set'>

# Way 2 = more common
set_value = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}

print(set_value)  # {1, 2, 3, 4, 5, 6, 7}
print(type(set_value))  # <class 'set'>

name = 'Yumi Ouchi'
set_value = set(name)
print(set_value)  # {'i', 'Y', 'h', ' ', 'u', 'O', 'm', 'c'}

list_sequence = [1, 2, 3, 3, 4, 5]
set_value = set(list_sequence)
print(set_value)  # {1, 2, 3, 4, 5}

tuple_sequence = (1, 2, 3, 3, 4, 5)
set_value = set(tuple_sequence)
print(set_value)  # {1, 2, 3, 4, 5}

# Verify if contain
if 3 in set_value:  # HAS
    print('HAS')
else:
    print('NO HAS')
# Important to remember duplicate value and not has sort

# List accepts duplicated value and it has 10 elements
list_value = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'List:{list_value} has {len(list_value)} elements')  # List:[99, 2, 34, 23, 2, 12, 1, 44, 5, 34] has 10 elements

# Tuple accepts duplicated value and it has 10 elements
tuple_value = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'List:{tuple_value} has {len(tuple_value)} elements')  # List:(99, 2, 34, 23, 2, 12, 1, 44, 5, 34) has 10
# elements

# Dictionary NOT accepts duplicated value and it has 8 elements
dictionary_value = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'List:{dictionary_value} has {len(dictionary_value)} elements')  # List:{99: 'dict', 2: 'dict', 34: 'dict',
# 23: 'dict', 12: 'dict', 1: 'dict', 44: 'dict', 5: 'dict'} has 8 elements

# Set NOT accepts duplicated value and it has 8 elements
set_value = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'List:{set_value} has {len(set_value)} elements')  # List:{1, 2, 99, 34, 5, 12, 44, 23} has 8 elements

# How any other set in Python we can mix Sets

set_value = {1, 'b', True, 34.22, 44}
print(set_value)  # {1, 34.22, 44, 'b'}
print(type(set_value))  # <class 'set'>

# We can iterate the set
for value in set_value:
    print(value, end=', ')  # 1, 34.22, 44, b,

country = ['Belo Horizonte', ' Sao Paulo', 'Cuiaba', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande']
print(country)  # ['Belo Horizonte', ' Sao Paulo', 'Cuiaba', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande']
print(len(country))  # 7

# how many distinct countries
print(len(set(country)))  # 5

# Add elements at sets

set_value = {1, 2, 3}
set_value.add(4)
set_value.add(4)
print(set_value)  # {1, 2, 3, 4}


# Way 1
set_value.remove(1)  # inform the value and not index
print(set_value)  # {2, 3, 4}

# If not found show KeyError and not return value

# Way 2
set_value.discard(2)
print(set_value)  # {3, 4}
set_value.discard(22)

# If not fount no error is showing


value_set = {1, 2, 3}
print(value_set)  # {1, 2, 3}

# Copy sets
# Way 1 - Deep Copy
new_set = value_set.copy()
print(new_set)  # {1, 2, 3}

new_set.add(4)

print(new_set)  # {1, 2, 3, 4}
print(value_set)  # {1, 2, 3}
# Way 2 - Shallow Copy
new_set = value_set
print(new_set)  # {1, 2, 3}

new_set.add(4)

print(new_set)  # {1, 2, 3, 4}
print(value_set)  # {1, 2, 3, 4}
value_set = {1, 2, 3}
print(value_set)  # {1, 2, 3}

# Remove all the elements of set
value_set.clear()
print(value_set)  # set()

# Mathematics
student_python = {'Ana', 'Maria', 'Fernando', 'Pedro', 'Julia'}
student_java = {'Patricia', 'Julia', 'Ana', 'Ellen', 'William', 'Bob'}

# BETTER
# Way 1 - Union => create a set with name with single name
union_student = student_java.union(student_python)
print(union_student)  # {'Bob', 'Ana', 'William', 'Pedro', 'Maria', 'Julia', 'Ellen', 'Fernando', 'Patricia'}

# Way 2 - pipe | character
union_student2 = student_python | student_java
print(union_student2)  # {'Bob', 'Ana', 'William', 'Pedro', 'Maria', 'Julia', 'Ellen', 'Fernando', 'Patricia'}

# Wrong => student_python + student_java

# BETTER
# Way 1 - Intersection
intersection_student = student_java.intersection(student_python)
print(intersection_student)  # {'Ana', 'Julia'}

# Way 2 - & character
intersection_student2 = student_python & student_java
print(intersection_student2)  # {'Ana', 'Julia'}

# BETTER
# DIFFERENCE => set whats is not in another
difference_student = student_java.difference(student_python)
print(difference_student)  # {'Patricia', 'William', 'Bob', 'Ellen'}

difference_student = student_python.difference(student_java)
print(difference_student)  # {'Fernando', 'Pedro', 'Maria'}
"""
# Mathematics
student_python = {'Ana', 'Maria', 'Fernando', 'Pedro', 'Julia'}
student_java = {'Patricia', 'Julia', 'Ana', 'Ellen', 'William', 'Bob'}

# Sum*, Max Value*, Min Value*, Size (* All are integer or float)

set_value = {1, 2, 3, 4, 5}
print(sum(set_value))  # 15
print(min(set_value))  # 1
print(max(set_value))  # 5
print(len(set_value))  # 5
