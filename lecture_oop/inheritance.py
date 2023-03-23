###### Приклад наслідування класу
class Shape:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

rectangle = Rectangle("red", 5, 10)
circle = Circle("blue", 7)

print(rectangle.area())  # Output: 50
print(circle.area())  # Output: 153.86
print(dir(circle))
print(circle.color)


####### Приклад наслідування від бібліотечного класу
class MyList(list):
    # def __init__(self, elements=[]):
    #     super().__init__(elements)
    # розширили клас
    def get_first(self):
        if len(self) > 0:
            return self[0]
        else:
            raise IndexError('MyList index out of range')
    # перевизначили метод
    def append(self, element):
        self.insert(0, element)

# Створення екземпляру класу MyList
my_list = MyList([1, 2, 3, 4, 5])

# Використання методу get_first()
print(my_list.get_first())  # 1

# Використання успадкованих методів класу list
my_list.append(3)
print(my_list)

my_list.sort()
print(my_list)

empty_list = MyList()
#print(empty_list.get_first())
empty_list.append(4)
empty_list.extend([1,2])
print(empty_list, empty_list.get_first())


###### Наслідування від множинного класу
class A:
    def foo(self):
        print("A")

class B:
    def foo(self):
        print("B")

class C(A, B):
    pass

c = C()
c.foo() # виведе "A"
