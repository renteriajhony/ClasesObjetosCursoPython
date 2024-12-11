
class Persona:
    atributo_clase: int = 0
    
    def __init__(self, atributo_instamcia: str):
        self.atributo_instamcia = atributo_instamcia
        
if __name__ == '__main__':
    print('*** Atributis de clase ***')
    print(Persona.atributo_clase)
    print('*** Atributis de clase ***')
    persona = Persona('Atributo instancia')
    Persona.atributo_clase = 10
    print(persona.atributo_instamcia)
    print(persona.atributo_clase)