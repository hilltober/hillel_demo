from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(ABC):
    @abstractmethod
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def interface_a(self):
        return "ConcreteProductA1"


class ConcreteProductA2(AbstractProductA):
    def interface_a(self):
        return "ConcreteProductA2"


class AbstractProductB(ABC):
    @abstractmethod
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    def interface_b(self):
        return "ConcreteProductB1"


class ConcreteProductB2(AbstractProductB):
    def interface_b(self):
        return "ConcreteProductB2"


def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.interface_a(), product_b.interface_b())


if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    client_code(factory1)

    factory2 = ConcreteFactory2()
    client_code(factory2)

# У цьому прикладі клас AbstractFactory визначає інтерфейс для створення
# об’єктів (тобто create_product_a та create_product_b).
# Класи ConcreteFactory1 і ConcreteFactory2 реалізують ці методи
# для повернення об’єктів ConcreteProductA1, ConcreteProductB1,
# ConcreteProductA2, та ConcreteProductB2 відповідно.

# Класи AbstractProductA та AbstractProductB визначають інтерфейси
# для продуктів A і B відповідно. У той час як класи
# ConcreteProductA1, ConcreteProductA2, ConcreteProductB1 та ConcreteProductB2
# забезпечують конкретні реалізації цих продуктів. Функція client_code є
# кодом клієнта, що використовує фабрику та її продукцію.

# Блок if __name__ == "__main__" є точкою входу програми.
