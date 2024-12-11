
class Animal:
    def hacer_sonido(self):
        print('Animal hacer sonido')

class Dog(Animal):
    def hacer_sonido(self):
        print('Perro hacer sonido')

class Cat(Animal):
    def hacer_sonido(self):
        print('Gato hacer sonido')

def hacer_sonido_animal(animal: Animal):
    animal.hacer_sonido()

if __name__ == '__main__':
    print('*** Ejemplo Polimorfismo ***')
    print('Clase Animal')
    animal = Animal()
    animal.hacer_sonido()
    print('\nClase Perro')
    perro = Dog()
    perro.hacer_sonido()
    print('\nClase Gato')
    cat = Cat()
    cat.hacer_sonido()
    print('\nHacer sonido animal Funcion Polimorfica')
    hacer_sonido_animal(animal)
    hacer_sonido_animal(perro)
    hacer_sonido_animal(cat)