
class Persona:
    # Atributo de clase
    contador_personas: int = 0

    def __init__(self, nombre, apellido):
            Persona.contador_personas += 1
            self.id = Persona.contador_personas
            self.nombre = nombre
            self.apellido = apellido

    def mostrar_persona(self):
        print(f''' Persona:
        Id: {self.id}
        Nombre: {self.nombre}
        Apellido: {self.apellido} ''')


    #Metodo de clase
    @staticmethod
    def get_contador_personas_estatico():
        print('*** Metodo statico ***')
        return Persona.contador_personas
    @classmethod
    def get_contador_personas_clase(cls):
        print('*** Metodo de clase ***')
        return cls.contador_personas

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Marin')
    persona1.mostrar_persona()

    persona2 = Persona('Julio', 'Voltio')
    persona2.mostrar_persona()

    print(f'\nCantidad de personas creadas : {Persona.contador_personas}')
    persona3 = Persona('Jhony', 'Jolker')
    persona3.mostrar_persona()
    print(f'\nCantidad de personas creadas : {Persona.contador_personas}')
    print(f'Contador de objetos (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador de objetos (class): {Persona.get_contador_personas_clase()}')