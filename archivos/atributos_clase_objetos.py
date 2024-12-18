
class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Persona Nombre: {self.nombre} - Apellido: {self.apellido}'

persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__)

#Crear un atributo al vuelo
print(persona1.contador_personas)
persona1.contador_personas = 10
print(persona1.__dict__)
# El atributi anterior oculta al atributo de clase
print(persona1.contador_personas)# Atributo de objeto
print(Persona.contador_personas)# Atributo de clase
persona2 = Persona('Olga', 'Marin')
print(persona2.__dict__)