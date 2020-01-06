"""
Any and All

all() -> return True if all the elements of iterative are true or if is empty

# Sample all()
print(all([0, 1, 2, 3, 4]))  # all the element are True? False
# 0 - False, 1- True, 2- True, 3- True, 4 True

print(all([1, 2, 3, 4]))  # all the element are True? True
print(all((1, 2, 3, 4)))  # all the element are True? True
print(all({1, 2, 3, 4}))  # all the element are True? True
print(all('Geek'))  # all the element are True? True
print(all([]))  # all the element are True? True

names = ['Carla', 'Carlos', 'Caio', 'Cristina']
print(all([name[0] == 'C' for name in names]))  # True


# OBS: the iterative empty convert to bool is False, but all() understands as True
result = [character for character in 'eiof' if character in 'aeiou']
print(result)  # ['e', 'i', 'o']
print(all(result))  # True

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))  # True

any() -> Return True if any element is iterative to True. If the iterative is empty, return False

"""
print(any([0, 1, 2, 3, 4]))  # True
print(any([]))  # False
print(any([0, False, {}, (), []]))  # False
names = ['Carla', 'Carlos', 'Caio', 'Cristina', 'Vanessa']

print(any([name[0] == 'C' for name in names]))  # True

print(any([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))  # True





