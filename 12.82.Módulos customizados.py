"""
Custom models

Modules are Python file

# import specific module
from funções_com_parametros import odd_sum

print(odd_sum([1, 2, 3, 4, 5, 6, 7]))

import funções_com_parametros as fcp

# We are access and print module value
print(fcp.list_value)
print(fcp.tuple_value)
print(fcp.odd_sum(fcp.list_value))
"""

from mapas import values

print(list(map(values)))
