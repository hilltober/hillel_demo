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


class MyFileReader:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip()
        else:
            self.file.close()
            raise StopIteration


class MyGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for value in range(self.start, self.end):
            yield value
