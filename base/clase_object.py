class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f''' Persona: 
        Nombre: {self.nombre} 
        Apellido: {self.apellido}
        Dir. Mem: {super.__str__(self)}
        '''

if __name__ == '__main__':
    persona = Persona("Jhony", "Renteria")
    print(persona)