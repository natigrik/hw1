class Figure(object):
    name = None
    area = None
    perimeter = None
    figures = ['triangle', 'rectangle', 'circle', 'square']
    _abstract = True

    def __init__(self):
        if self._abstract:
            raise NotImplementedError('Cannot instantiate abstract base class')

    def add_area(self, figure):
        if figure.name not in Figure.figures:
            raise ValueError('Wrong class!')
        else:
            return self.area + figure.area
