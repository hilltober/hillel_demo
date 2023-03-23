###### Polymorphism of methods
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(10)]
for shape in shapes:
    print(shape.area())

####### Polymorphism of operators
print(5 + 6)  # prints: 11
print('Hello, ' + 'world!')  # prints: Hello, world!

######## Polymorphism of functions
print(len('Hello'))  # prints: 5
print(len([1, 2, 3]))  # prints: 3

####### Polymorphism through inheritance
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'Woof!'

class Cat(Animal):
    def speak(self):
        return 'Meow!'

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())


'''
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
'''
