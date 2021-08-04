import math
from Figure import Figure


class Triangle(Figure):
    name = "triangle"

    # def __init__(self, first_side, second_side, third_side):
    #     if ((first_side < second_side + third_side) and (second_side < first_side + third_side)
    #             and (third_side < first_side + second_side)):
    #         self.first_side = first_side
    #         self.second_side = second_side
    #         self.third_side = third_side
    #     else:
    #         raise ValueError

    def __init__(self, first_side, second_side, third_side):
        pass

    def __new__(cls, first_side, second_side, third_side):
        if (first_side < second_side + third_side) and (second_side < first_side + third_side) and (third_side < first_side + second_side):
            cls.first_side = first_side
            cls.second_side = second_side
            cls.third_side = third_side
            return super().__new__(cls)

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
print(type(tr))
# print(tr.first_side, tr.second_side, tr.third_side)
# print(tr.area)
# print(tr.perimeter)
