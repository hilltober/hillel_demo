class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("Side should be a positive number")
        self._side = value

    def area(self):
        return self._side ** 2

sq = Square(5)
print(sq.side)  # 5
print('_', sq._side)

sq.side = 10
print(sq.side)  # 10


# Using property()
# class property(fget=None, fset=None, fdel=None, doc=None)
class C:
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x)

c = C()
c.x = 5
print(c.x)


'''
У Python енкапсуляція - це механізм, який дозволяє об'єднати дані та методи, 
які з ними пов'язані, в один компонент, та забезпечує доступ до них лише через 
публічний інтерфейс. Це означає, що дані та методи, що містяться внутрішньо, не
 доступні для безпосереднього звернення з зовнішнього середовища. Замість 
 цього, доступ до них можна отримати через методи, які називаються "гетерами" 
 та "сетерами", які надаються у публічному інтерфейсі.
'''
