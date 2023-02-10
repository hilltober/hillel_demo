class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


if __name__ == "__main__":
    pet = get_pet("dog")
    print(pet.speak())

    pet = get_pet("cat")
    print(pet.speak())

# У цьому прикладі класи Dog і Cat є конкретними реалізаціями домашніх тварин.
# Функція get_pet є фабричним методом, який повертає екземпляр
# Собаки або Кота на основі переданого рядкового аргументу.

# Блок if __name__ == "__main__" є точкою входу програми.

# Коли програма запускається, вона створює екземпляри Dog та Cat
# і викликає їхні методи speak, щоб надрукувати відповідні звуки.
