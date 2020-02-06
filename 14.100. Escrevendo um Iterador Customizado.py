"""
Writing a custom iterator

to create a iterator we have to have __iter__ and __next__

"""

class Count:
    def __init__(self, minor, major):
        self.minor = minor
        self.major = major
    def __iter__(self):
        return self
    def __next__(self):
        if self.minor < self.major:
            number = self.minor
            self.minor = self.minor + 1
            return number
        raise StopIteration




counter = Count(1, 51)

print(counter.major)  # 51

it = iter(counter)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
print(next(it))  # 5
print(next(it))  # 6
