from curses.textpad import rectangle

from herencia_multiple.rectangle import Rectangle
from herencia_multiple.square import Square

print('Creacion de Objeto cuadrado'.center(50,'-'))
square = Square(2, 'rojo')
print(f'Area del cuadrado: {square.area()}')
print(f'{square}')

print('Creacion de Objeto Rectangulo'.center(50,'-'))
rectangle = Rectangle(3, 11, 'Verde')
rectangle.height = 12
print(f'Area del Rectangulo: {rectangle.area()}')
print(f'{rectangle}')

#MRO - Method Resolution Order
# print(Square.mro())