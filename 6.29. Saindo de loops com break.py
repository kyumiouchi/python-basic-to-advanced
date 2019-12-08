"""
Take out of loop with break

Works like Java and C

Break works to get out of the loop
"""

# Sample 1

for number in range(1, 11):
    if number == 6:
        break
    else:
        print(number, end=", ")
print("get out of loop")  # 1, 2, 3, 4, 5, get out of loop

# Sample 2

while True:
    command = input('Write "exit" to break: ')
    if command == "exit":
        break
