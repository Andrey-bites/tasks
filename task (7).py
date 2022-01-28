""" Модифицируйте класс Point следующим образом:
обеспечьте проверку значений координат (только числа),
добавьте метод, который бы позволял сравнивать точки(если координаты точек совпадают - точки равны) """


class Point:
    _x = 0
    _y = 0

    def __init__(self, x, y):
        self._x, self._y = x, y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # def __repr__(self):
    #     return f'Point with x is {self._x} and y is {self._y}'

    def __eq__(self, other):

        if other._x is not self._x or other._y is not self._y:
            print('Точки не равны')
            return False
        else:
            print('Точки равны')
            return True

    def __str__(self):
        return f'Point with x is {self._x} and y is {self._y}'

    def __add__(self, other):

        if other.__class__ is not self.__class__:
            raise Exception
        return Line(self, other)


p1 = Point(13, 20)
p2 = Point(5, 5)
p3 = Point(5, 5)
print(p1 == p3)
print(p1 == p2)
print(p2 == p3)
print(p1)
print(p1.x)
print(p1.y)

res = str(p1)
print(res)

""" Модифицируйте класс Line следующим образом: обеспечьте проверку точек
начала и конца при создании линии в __init__ (точки начала и конца отрезка не должны совпадать)
модифицируйте метод __str__ так чтобы он отдавал информацию в формате
("Line with points [информация о точке начала] [информация о точке конца] and length [длина]") """


class Line:
    _start_point = Point(0, 0)
    _finish_point = Point(0, 0)

    def __init__(self, first_point, second_point):

        if not isinstance(first_point, Point) or \
                not isinstance(second_point, Point) or \
                not self._check_points_coord(first_point, second_point):
            raise Exception

        self._start_point = first_point
        self._finish_point = second_point

    def length(self):
        return ((self._start_point.x - self._finish_point.x)**2 + (self._start_point.y - self._finish_point.y) ** 2) ** 0.5

    @staticmethod
    def _check_points_coord(p1, p2):
        return not (p1.x == p2.x and p1.y == p2.y)

    @classmethod
    def get_default(cls):
        return cls._start_point, cls._finish_point

    def __getattribute__(self, attrname):
        print(f'in __getattribute__ with {attrname}')
        return object.__getattribute__(self, attrname)

    def __setattr__(self, key, value):
        print(f'in __setattr__ with {key} {value}')
        return object.__setattr__(self, key, value)

    def __getitem__(self, item):  # a['b']
        print(f'in __getitem__ with {item}')
        return getattr(self, item, None)

    def __setitem__(self, item, val):  # a['b'] = c
        print(f'in __setitem__ with {item} {val}')
        return setattr(self, item, val)

    def __contains__(self, item):  # in
        print(f'in __contains__ with {item}')
        return

    def __eq__(self, other):  # ==
        print(f'in __eq__ with {other}')

        if other.__class__ is not self.__class__:
            raise Exception
        return self.length() == other.length()

    def __str__(self):
        return f'Line with points ({self._start_point}) and ({self._finish_point}) and length {self.length()}'


line1 = Line(p1, p2)
line2 = p1 + p2
res = str(line1)
print(res)

""" * Допишите класс Unit: добавьте метод hit, который принимает обьект класса Unit,
и наносит ему повреждения. удары юнита должны только уменьшать здоровье атакуемого юнита!
на величину собственной атаки минус защита атакуемого юнита.
добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было установить < 0
(например у юнита осталось 5 здоровья а его ударили на 10) """


class Unit:
    _name = 'Bil'
    _health = 100
    _attack = 100
    _protection = 100

    def __init__(self, init_name=None, init_health=None, init_attack=None,
                 init_protection=None):
        if init_name is not None:
            self._name = init_name
            if not isinstance(self._name, str):
                raise Exception('name must be a string')

        if init_health is not None:
            self._health = init_health
            if not isinstance(init_health, int):
                raise Exception('health must be a intager')

        if init_attack is not None:
            self._attack = init_attack
            if not isinstance(init_attack, int):
                raise Exception('attack must be a intager')

        if init_protection is not None:
            self._protection = init_protection
            if not isinstance(init_protection, int):
                raise Exception('protection must be a intager')

    def _get_dmg():
        pass

    def _get_protection():
        pass

    def hit(self, enemy):
        # todo: check enemy type
        # todo: check enemy health
        dmg = self._get_dmg
        # todo: check dmg > 0
        enemy._health -= dmg
        if self._health < 0:
            self._health = 0
            print('Ahhhhhhh')
        return enemy._health

    def unit_info(self):
        print(
            f'Имя: {self._name}. Здоровье: {self._health} ХП. Атака: {self._attack} Урона. Защита: {self._protection} Брони.')


class Knight(Unit):
    pass


class Mage(Unit):
    pass
