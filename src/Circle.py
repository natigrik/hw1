from Figure import Figure


class Circle(Figure):
    name = "circle"

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        s = (self.radius ** 2) * 3.14
        return s.__round__(2)

    @property
    def perimeter(self):
        per = self.radius * 2 * 3.14
        return per.__round__(2)


circle = Circle(4)
print(circle.area)
print(circle.perimeter)
