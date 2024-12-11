from herencia_multiple.color import Color
from herencia_multiple.geometric_figure import GeometricFigure


class Square(GeometricFigure, Color):
    def __init__(self, side, color):
        #Todo: Genera confucion, ya que no sabe que constructor inicializa
        # super().__init__(side, side)
        # super().__init__(color)
        GeometricFigure.__init__(self, side, side)
        Color.__init__(self, color)

    def __str__(self):
        return f'{GeometricFigure.__str__(self)} {Color.__str__(self)}'

    def area(self):
            return self.width * self.height

