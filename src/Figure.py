class Figure:
    name = None
    area = None
    perimeter = None

    def get_area(self):
        return self.area

    def add_area(self, figure):
        if figure not in ("triangle", "rectangle", "square", "circle"):
            raise ValueError('Wrong class!')
        else:
            return self.area + figure.area
