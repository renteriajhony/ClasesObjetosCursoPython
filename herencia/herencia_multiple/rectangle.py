from herencia.herencia_multiple.color import Color
from herencia.herencia_multiple.geometric_figure import GeometricFigure


class Rectangle(GeometricFigure, Color):
    def __init__(self, width, heigth, color):
        GeometricFigure.__init__(self, width, heigth)
        Color.__init__(self, color)

    def __str__(self):
        return f'{GeometricFigure.__str__(self)} {Color.__str__(self)}'

    def area(self):
            return self.width * self.height

