t = __import__('2')


class Rectangle(t.Shape):
    def __init__(self, length, width):
        self.length, self.width = length, width
        self.compute_area()

    def compute_area(self):
        self.area = self.length*self.width


x = Rectangle(5, 6)
x.compute_area()
x.print_area()