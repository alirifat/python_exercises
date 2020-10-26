class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

p1 = Point(3, 5)
p2 = Point(5, 3)
print(p1 + p2)
