class Point:
    _x = 0
    _y = 0

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self._x = x
            self._y = y
        else:
            raise TypeError

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self._x = value
        else:
            raise TypeError

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self._y = value
        else:
            raise TypeError

    def __str__(self):
        return f'Point [{self.x}:{self.y}]'

p1 = Point(0,0)
p2 = Point(4,0)
p3 = Point(0,3)
print(p1, p2, p3)
# p1.x = 'string' #поламаємося

class Triangle:
    _point_1 = None
    _point_2 = None
    _point_3 = None

    def point1_getter(self):
        return self._point_1

    def point1_setter(self, value):
        if isinstance(value, Point):
            self._point_1 = value
        else:
            raise TypeError

    point1 = property(point1_getter, point1_setter)

    def point2_getter(self):
        return self._point_2

    def point2_setter(self, value):
        if isinstance(value, Point):
            self._point_2 = value
        else:
            raise TypeError

    point2 = property(point2_getter, point2_setter)

    def point3_getter(self):
        return self._point_3

    def point3_setter(self, value):
        if isinstance(value, Point):
            self._point_3 = value
        else:
            raise TypeError

    point3 = property(point3_getter, point3_setter)


    def __init__(self, point_1, point_2, point_3):
        self._point_1 = point_1
        self._point_2 = point_2
        self._point_3 = point_3

    def side_length(self, point1, point2):
        diffx = point1.x - point2.x
        diffy = point1.y - point2.y
        return (diffx ** 2 + diffy ** 2) ** 0.5

    def triangle_area(self):
        a = self.side_length(self.point1, self.point2)
        b = self.side_length(self.point2, self.point3)
        c = self.side_length(self.point3, self.point1)
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area

triangle1 = Triangle(p1, p2, p3)
print(triangle1.triangle_area())