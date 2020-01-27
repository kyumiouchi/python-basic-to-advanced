def function1():
    print('1)Yumi Ouchi')


if __name__ == '__main__':
    function1()
    print('first.py direct execution')
else:
    print(f'first.py was imported {__name__}')
