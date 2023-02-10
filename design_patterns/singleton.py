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

# У цьому прикладі клас Singleton має змінну рівня класу _instance,
# що містить єдиний екземпляр класу.
# Метод __new__ перевизначено, щоб повернути єдиний екземпляр класу,
# якщо він існує, або створити новий екземпляр класу, якщо це не так.

# Блок if __name__ == "__main__" є точкою входу програми.

# Коли програма виконується, вона створює два екземпляри класу Singleton
# і друкує True, якщо це однаковий екземпляр (підтвердження правильності роботи
# шаблону singleton).
