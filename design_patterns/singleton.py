class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)

# In this example, the Singleton class has a class-level variable _instance
# that holds the single instance of the class. The __new__ method is overridden
# to return the single instance of the class if it exists, or create a new
# instance of the class if it doesn't.
# The if __name__ == "__main__" block is the entry point of the program.
# When the program is run, it creates two instances of the Singleton class
# and prints True if they are the same instance,
# confirming that the singleton pattern is working correctly.
