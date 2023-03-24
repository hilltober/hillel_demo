class Number:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        return NotImplemented

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return f"Number({self._value})"


num1 = Number(5)
num2 = Number(3)

# perform operations and print results
print(num1 + num2)  # 8
print(num1 - num2)  # 2
print(num1 * num2)  # 15
print(num1 / num2)  # 1.6666666666666667


class MyList(list):
    def __sub__(self, other):
        return MyList([x for x in self if x not in other])

    def __add__(self, other):
        return MyList(super().__add__(other))

    def __mul__(self, other):
        return MyList(super().__mul__(other))

    def __str__(self):
        return f"MyList({super().__str__()})"

    def __repr__(self):
        return f"MyList({super().__repr__()})"


list1 = MyList([1, 2, 3, 4])
list2 = MyList([3, 4, 5, 6])

# subtract the lists and print the result
result = list1 - list2
print(result)  # MyList([1, 2])

# add the lists and print the result
result = list1 + list2
print(result)  # MyList([1, 2, 3, 4, 3, 4, 5, 6])

# multiply the list and print the result
result = list1 * 3
print(list(result))  # MyList([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
