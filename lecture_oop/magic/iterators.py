class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


print(MyRange(10, 20).__next__())
x = MyRange(16, 20)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())

for i in MyRange(1, 5):
    print(i)


class MyFileReader:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __next__(self, iteration=StopIteration):
        line = self.file.readline()
        if line:
            return line.strip()
        else:
            self.file.close()
            raise iteration


for i in MyFileReader('test.txt'):
    print(i)
