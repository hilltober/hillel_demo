class Person:
    # Атрибут класу
    species = "human"

    def __init__(self, name, age):
        # Атрибути об'єкту
        self.name = name
        self.age = age

    # Метод класу
    @classmethod
    def get_species(cls):
        return cls.species  # Person.species

    # Метод об'єкту
    def get_name(self):
        return self.name


h1 = Person('Vitaii', 34)
print(Person.species)
print(Person.get_species())
print(h1.get_species())
print(h1.species)


# Приклад classmethod
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    @classmethod
    def from_string(cls, time_string):
        hour, minute = map(int, time_string.split(":"))
        return cls(hour, minute)

    @classmethod
    def from_datetime(cls, datetime_obj):
        hour = datetime_obj.hour
        minute = datetime_obj.minute
        return cls(hour, minute)


# Створення об'єкту з рядка даних
time_string = "23:45"
time = Time.from_string(time_string)
print(time)  # 23:45

# Створення об'єкту з об'єкта datetime
import datetime

datetime_obj = datetime.datetime(2023, 3, 19, 23, 45)
time = Time.from_datetime(datetime_obj)
print(time)  # 23:45
