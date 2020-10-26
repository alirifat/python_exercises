class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        if isinstance(other, tuple):
            return self.add_tuple(other)
    def __radd__(self, other):
        return self.__add__(other)
    def add_point(self, other):
        temp = Point(self.x, self.y)
        temp.x += other.x
        temp.y += other.y
        return temp
    def add_tuple(self, other):
        temp = Point(self.x, self.y)
        temp.x += other[0]
        temp.y += other[1]
        return temp


p = Point(3,5)
t = Point(4,4)
print(p + (2,2))
print((2,2) + p)

print(getattr(p, 'x'))
