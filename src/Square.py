from Figure import Figure


class Square(Figure):
    name = "square"

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        s = self.side ** 2
        return s.__round__(2)

    @property
    def perimeter(self):
        per = self.side * 4
        return per.__round__(2)


square = Square(5)
print(square.area, square.perimeter)
print(square.name)
print(square.add_area(square))
