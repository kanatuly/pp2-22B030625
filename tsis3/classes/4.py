class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, new_x, new_y):
        self.__init__(new_x, new_y)

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


a = Point(4, 4)
b = Point(8, 8)
a.show()
b.show()
print(a.dist(b), b.dist(a))
b.move(10, -4)
b.show()
print(a.dist(b), b.dist(a))