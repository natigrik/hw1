from Figure import Figure


class Square(Figure):
    name = "square"
    _abstract = False

    def __init__(self, side):
        super().__init__()
        self.side = side

    @property
    def area(self):
        s = self.side ** 2
        return s.__round__(2)

    @property
    def perimeter(self):
        per = self.side * 4
        return per.__round__(2)
