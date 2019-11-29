"""
Receive data User

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

'__builtins__' -> language integrated features

print(dir(__builtins__))
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

input() -> All data comes from input is String

In Python, String is everything is between:
- Single Quotation marks
- Double quotation marks
- Triple Single Quotation marks
- Triple Double quotation marks

Samples:
- Single Quotation marks -> 'Yumi'
- Double quotation marks -> "Yumi"
- Triple Single Quotation marks -> '''Yumi'''
- Triple Double quotation marks -> " " "Yumi" " "(without space)
"""
# Data Input
# print("Qual seu nome?")
# name = input()
name = input("Qual seu nome? ")

# Sample old version -> 2.x
# print('Seja bem-vinda %s' % name)

# Sample new version -> 3.x
# print('Seja bem-vinda {0}'.format(name))

# Sample new version -> 3.7
print(f'Seja bem-vinda {name}')

# print("Qual sua idade?")
# age = input()
# age = input("Qual sua idade? ")
age = int(input("Qual sua idade? "))

# Output
# Sample old version -> 2.x
# print('The %s has %s years' % (name, age))

# Sample new version -> 3.x
# print('The {0} has {1} years'.format(name, age))

# Sample new version -> 3.7
print(f'The {name} has {age} years')
"""
int(age) => cast

Cast is 'conversion' of data type to another
"""
print(f'The {name} has {2019 - age} years')
