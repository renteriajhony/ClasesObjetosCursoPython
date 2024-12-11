from typing import override

print('*** Ejemplo de herencia en python ***\n')
class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas al dia')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo Ladrar')

    def dormir(self):
        print('Duermo 15 horas al dia')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo Maullar')

if __name__ == '__main__':
    print('\n*** Soy Clase padre Animal ***\n')
    animal = Animal();
    animal.comer()
    animal.dormir()

    print('\n*** Soy Clase Hijo Perro ***\n')
    perro = Perro()
    perro.comer()
    perro.dormir()
    perro.hacer_sonido()