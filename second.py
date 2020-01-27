def function2():
    print('2)Yumi Ouchi')


if __name__ == '__main__':
    function2()
    print('second.py direct execution')
else:
    print(f'second.py was imported {__name__}')
