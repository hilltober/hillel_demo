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

# In this example, the AbstractFactory class defines the interface for creating
# objects (i.e., create_product_a and create_product_b).
# The ConcreteFactory1 and ConcreteFactory2 classes implement these methods
# to return objects of ConcreteProductA1, ConcreteProductB1, ConcreteProductA2,
# and ConcreteProductB2 respectively. The AbstractProductA and AbstractProductB
# classes define the interfaces for products A and B respectively,
# while the ConcreteProductA1, ConcreteProductA2, ConcreteProductB1,
# and ConcreteProductB2 classes provide concrete
# implementations of these products. The client_code function is the
# client code that uses the factory and its products.
# The if __name__ == "__main__" block is the entry point of the program.
