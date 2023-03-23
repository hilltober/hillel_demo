from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(shape.area())

# Інший спосіб реалізувати абстрактний метод
class Shape1:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

'''
Принцип абстракції - це принцип ООП, що полягає в тому, щоб виділити головні 
характеристики об'єкту і приховати від користувача деталі його реалізації. Це 
дозволяє спростити складну систему, розбити її на окремі компоненти, які можна 
змінювати без впливу на решту системи.

За допомогою абстракції можна представити об'єкти у вигляді інтерфейсу, який 
визначає поведінку об'єкту, а не його реалізацію. Інші об'єкти можуть 
використовувати цей інтерфейс, не звертаючись до деталей реалізації. Це 
дозволяє знизити залежність між компонентами системи, що зробить її більш 
масштабованою та легшою для розуміння.

Застосування принципу абстракції дозволяє зменшити складність коду та полегшити
 процес розробки, тестування та підтримки програмного забезпечення. В Python, 
 для реалізації абстракції використовуються абстрактні класи та інтерфейси.
'''
