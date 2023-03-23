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
        return f"Square with side length {self._side}"

    def __repr__(self):
        return f"Square({self._side})"

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.side == other.side
        return False

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.side < other.side
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Square):
            return self.side <= other.side
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.side > other.side
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.side >= other.side
        return NotImplemented


# create two square objects
sq1 = Square(5)
sq2 = Square(3)

# print the square objects using __str__ and __repr__
print(sq1)  # Square with side length 5
print(repr(sq2))  # Square(3)

# compare the square objects using the comparison operators
print(sq1 == sq2)  # False
print(sq1 != sq2)  # True
print(sq1 > sq2)  # True
print(sq1 >= sq2)  # True
print(sq1 < sq2)  # False
print(sq1 <= sq2)  # False

# change the side length of a square object
sq1.side = 4

# compare the square objects again
print(sq1 == sq2)  # False
print(sq1 != sq2)  # True
print(sq1 > sq2)  # True
print(sq1 >= sq2)  # True
print(sq1 < sq2)  # False
print(sq1 <= sq2)  # False
