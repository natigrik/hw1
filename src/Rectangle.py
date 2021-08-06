from src.Figure import Figure


class Rectangle(Figure):
    name = "rectangle"
    _abstract = False

    def __init__(self, first_side, second_side):
        super().__init__()

    def __new__(cls, first_side, second_side):
        if first_side > 0 and second_side > 0:
            cls.first_side = first_side
            cls.second_side = second_side
            return super().__new__(cls)

    @property
    def area(self):
        s = self.first_side * self.second_side
        return s.__round__(2)

    @property
    def perimeter(self):
        per = (self.first_side + self.second_side) * 2
        return per.__round__(2)
