"""
File open

r -> Open to read - Standard
w -> Write file and overwrite the exist file
x -> Open if exist, if not exist FileExistsError
a -> Open and Write file, add new information in the end
+ -> Update the read and write mode

# Sample X
try:
    with open('new.txt', 'x') as file:
        file.write('New data\n' * 10)
except FileExistsError:
    print('File exists')


#Sample A
with open('new.txt', 'a') as file:
    while True:
        fruit = input('Write down the fuit name or write exit:')
        if fruit != 'exit':
            file.write(fruit)
            file.write('\n')
        else:
            break

with open('new.txt', 'a') as file:
    # file.seek(0) not control the course
    file.write('fruit\n')
    file.write('jose\n')
    file.write('master\n')
"""
# sample r+
# Can control the course
with open('new.txt', 'r+') as file:
    file.write('fruit\n')
    file.seek(11)
    file.write('jose\n')
    file.write('master\n')

