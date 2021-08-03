import math
from Figure import Figure


class Triangle(Figure):
    name = "triangle"

    def __init__(self, first_side, second_side, third_side):
        if (first_side > second_side + third_side) or (second_side > first_side + third_side) or (third_side > first_side + second_side):
            name = None
        else:
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side

    @property
    def area(self):
        p = (self.first_side + self.second_side + self.third_side) / 2
        s = math.sqrt(p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side))
        return s.__round__(2)

    @property
    def perimeter(self):
        per = self.first_side + self.second_side + self.third_side
        return per.__round__(2)


tr = Triangle(5, 6, 7)
print(tr.area)
print(tr.perimeter)
