from src.Figure import Figure


class Circle(Figure):
    name = "circle"
    _abstract = False

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    @property
    def area(self):
        s = (self.radius ** 2) * 3.14
        return s.__round__(2)

    @property
    def perimeter(self):
        per = self.radius * 2 * 3.14
        return per.__round__(2)
