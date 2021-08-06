import math


from src.Figure import Figure


class Circle(Figure):
    name = "circle"
    _abstract = False

    def __init__(self, radius):
        super().__init__()

    def __new__(cls, radius):
        if radius > 0:
            cls.radius = radius
            return super().__new__(cls)

    @property
    def area(self):
        s = (self.radius ** 2) * math.pi
        return s.__round__(2)

    @property
    def perimeter(self):
        per = self.radius * 2 * math.pi
        return per.__round__(2)
