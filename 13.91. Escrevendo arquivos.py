"""
Writing file

# OBS: When read a file, we can not write. If write we can not read.

# OBS: after write the file, it is created


with open('new.txt', 'w') as file:
    file.write('New datas\n')
    file.write('Text \n')
    file.write('Last line')

file = open('new2.txt', 'w')

file.write('new2.txt')
file.write('new2.txt')

file.close()

with open('new.txt', 'w') as file:
    file.write('New data\n' * 1000)
"""

with open('new.txt', 'w') as file:
    while True:
        fruit = input('Write down the fuit name or write exit:')
        if fruit != 'exit':
            file.write(fruit)
            file.write('\n')
        else:
            break

