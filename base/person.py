class Person:
    """
   Clase que representa a una persona.

   Atributos:
       name (str): El nombre de la persona.
       last_name (str): Apellidod de la persona.
   """
    def __init__(self, name, last_name):
        self._name = name
        self._last_name = last_name


    def show_person(self):
        """
        Imprime los datos de la persona.

        Void:
            str: Name: Name, LastName: LastName.
        """
        print(f''' Detail Person:
            Name: {self._name}
            LastName: {self._last_name}''')
        id_person:int = id(self)
        print(f'Dir. memory person: {id_person}')
        print(f'Dir. memory person: {hex(id_person)}')


if __name__ == '__main__':
    person1 = Person('Martin', 'Smith')
    person1.show_person()

    person2 = Person(last_name='Valdez', name='Juan')
    person2.show_person()