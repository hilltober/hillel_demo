# kwargs в конструкторі через setattr
class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        for key, value in kwargs.items():
            setattr(self, key, value)


person1 = Person('John', 30, occupation='Programmer', country='USA')
print(person1.name)  # виведе: John
print(person1.age)  # виведе: 30
print(person1.occupation)  # виведе: Programmer
print(person1.country)  # виведе: USA


# Додати атрибути після створення об'єкта
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog('Buddy', 'Labrador')
setattr(dog1, 'age', 5)
print(dog1.age)  # виведе: 5

# getattr
name = getattr(dog1, 'name')
print('Name is', name)
