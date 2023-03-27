import math
from abc import ABC, abstractmethod

# ####### Polymorphism of operators
# print(5 + 6)  # prints: 11
# print('Hello, ' + 'world!')  # prints: Hello, world!

# ######## Polymorphism of functions
# print(len('Hello'))  # prints: 5
# print(len([111, 222, 33]))  # prints: 3

"""
Поліморфізм через успадкування полягає в тому, що класи можуть успадковувати
властивості і методи від батьківського класу і використовувати їх у своїй 
реалізації. Якщо клас успадковує метод з батьківського класу, то він може 
перевизначити його власною реалізацією, яка буде викликатися замість 
батьківського методу, якщо це необхідно.

Наприклад, якщо є клас "Тварина" з методом "говорити", то класи 
"Собака" і "Кіт", які успадковують цей метод, можуть перевизначити його і 
реалізувати свій власний спосіб виведення звуків для їх власних видів тварин. 
Таким чином, ми можемо використовувати ці класи з методом "говорити" в одному 
і тому ж контексті, але отримувати різні результати, що і є суть поліморфізму 
через успадкування.
"""


# Абстрактний клас
class Humanoid(ABC):
    @abstractmethod
    def greet(self):
        pass


class Human(Humanoid):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hey, I am human {self.name}')


class Employee(Human):
    def greet(self):
        print(f'Hey, I am employee {self.name}')


class Programmer(Human):
    def greet(self):
        print(f'Hey, I am programmer {self.name}')


human = Human('Vanya')
employee = Employee('Andrew')
programmer = Programmer('Artem')

humans = [human, employee, programmer]
for person in humans:
    assert isinstance(person, Human)
    person.greet()

print('------------------')


def greet(humanoid: Human):
    humanoid.greet()


greet(human)
greet(employee)
print('------------------')


class Shape:
    def __init__(self, **kwargs):
        self.radius = kwargs.get('radius')
        self.sideA = kwargs.get('sideA')
        self.sideB = kwargs.get('sideB')
        self.sideC = kwargs.get('sideC')

    def area(self):
        pass


class Circle(Shape):
    """
    :param radius
    :type int or float
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    """
    :param sideA or sideB or sideC: will be used first one --side of square
    :type int or float
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.sideA or self.sideB or self.sideC:
            self.__side = self.sideA or self.sideB or self.sideC
        else:
            raise KeyError(
                f'Parameter should be in (sideA, sideB, sideC).'
                f' Given: {kwargs}'
            )

    def area(self):
        return self.__side ** 2


class Rectangle(Shape):
    """
    :param sideA -- height
    :param sideB -- width
    :type int or float
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__sideA = self.sideA
        self.__sideB = self.sideB

    def area(self):
        return self.__sideA * self.__sideB


circle = Circle(radius=7)
square = Square(sideA=5)
rectangle = Rectangle(sideA=5, sideB=6)

for shape in [circle, square, rectangle]:
    assert isinstance(shape, Shape)
    print(shape.area())

sqr = Square(vasya=5)
print(sqr.area())
