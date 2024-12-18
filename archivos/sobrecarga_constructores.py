#Simulacion de sobrecarga de constructores
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Persona Nombre: {self.nombre} - Apellido: {self.apellido}'

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

persona1 = Persona('Juan', 'Perez')
print(persona1)
print(Persona.crear_persona_vacia())
print(Persona.crear_persona_con_valores('Mark', 'Anthony'))