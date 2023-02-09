class Shape:
    area = 0
    def print_area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = length*length
"""
t = Square(12)
t.print_area()
x = Shape()
x.area = 213
x.print_area()
"""