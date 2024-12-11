#Todo: Para volver una clase abstracta debemos eredar de ABC (Abstrct Base Class)
#Para volver un metodo abstracto debemos utilizar el decorador abstractmethod

from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    def __init__(self, width, height):

        self._width = width if width > 0 and width <= 10 else 0
        self._height = height if height > 0 and height <= 10 else 0

    def __str__(self):
        return f'[Alto: {self._width}, Ancho: {self._height}]'

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        self._width = width if width > 0 and width <= 10 else 0

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height if height > 0 and height <= 10 else 0

    @abstractmethod
    def area(self):
        pass