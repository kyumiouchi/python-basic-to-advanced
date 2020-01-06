"""
Reduce

OBS: Reduce is not build-in in Python3+. We have to import and use the module 'functools'

99% of the time... for is more readable than reduce()

To understand the reduce()

# imagine you have to collect data:
data = [a1, a2, a3,.., an]

# Function receive 2 parameters

def function(x, y):
    return x*y

As map() and filter() the reduce() receive 2 parameters: function and iterable

reduce(function, data)

Reduce:

    Step 1: result1 = f(a1, a2)  # Apply the function with two first elements to wait the result
    Step 2: result2 = f(result1, a3)  # apply the function with the result before

    And repeat until the final
    Step 3: result 3 = f(result2, d4)

function(function(function(a1, a2), a3), a4)
"""
from functools import reduce

data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 23, 28]

mult = lambda x, y: x * y

result = reduce(mult, data)
print(result)  # 44401996800

# loop normal

res = 1

for n in data:
    res = res * n

print(res)  # 44401996800



