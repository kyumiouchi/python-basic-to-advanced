"""
Maps -> As known as dictionary


"""

values = {'jan': 100, 'fev': 200, 'mar': 300}

# Iteration
for key in values:  # jan, fev, mar,
    print(key, end=', ')
print()

# INCORRECT
for key in values:  # 100, 200, 300,
    print(values[key], end=', ')

print()
for key in values:  # In jan earn 100, In fev earn 200, In mar earn 300,
    print(f'In {key} earn {values[key]}', end=', ')
print()

print(values.keys())

# CORRECT
for key in values.keys():  # jan, fev, mar,
    print(key, end=', ')
print()

for value in values.values():  # 100, 200, 300,
    print(value, end=', ')
print()


print(values.items())  # dict_items([('jan', 100), ('fev', 200), ('mar', 300)])
for key, value in values.items():  # In jan earn 100, In fev earn 200, In mar earn 300,
    print(f'In {key} earn {value}', end=', ')
print()

# Sum*, Max value*, Min value*, size  (* integer or float)
print(sum(values.values()))  # 600
print(min(values.values()))  # 100
print(max(values.values()))  # 300
print(len(values))  # 3
