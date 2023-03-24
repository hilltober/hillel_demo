class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("Side should be a positive number")
        self._side = value

    def area(self):
        return self._side ** 2

    def __str__(self):
        return f'Square with side length {self._side}'

    def __repr__(self):
        return f'Square({self._side})'

# Create a square object
s = Square(5)

# Using __str__ to print a readable representation of the square
print(str(s))
# Output: "Square with side length 5"

# Using __repr__ to get a string representation that can recreate the object
print(repr(s))
# Output: "Square(5)"

# Using __repr__ with eval() to recreate the square object
s2 = eval(repr(s))
print(str(s2))
# Output: "Square with side length 5"

# Using __repr__ with exec() to recreate the square object
exec_str = f"s3 = {repr(s)}"
exec(exec_str)
print('--')
print(str(s3))
print('--')
# Output: "Square with side length 5"
