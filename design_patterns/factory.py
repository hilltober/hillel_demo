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

# In this example the Dog and Cat classes are concrete implementations of pets.
# The get_pet function is a factory method that returns an instance
# of either a Dog or a Cat based on the string argument passed to it.
# The if __name__ == "__main__" block is the entry point of the program.
# When the program is run, it creates instances of Dog and Cat
# and calls their speak methods to print their respective sounds.
