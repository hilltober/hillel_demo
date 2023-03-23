class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    result = MathUtils.add(3, 5)
    print(result)  # виведе 8

    result = MathUtils.multiply(2, 4)
    print(result)  # виведе 8

    mu = MathUtils()
    result = mu.multiply(2, 4)
    print(result)  # виведе 8
