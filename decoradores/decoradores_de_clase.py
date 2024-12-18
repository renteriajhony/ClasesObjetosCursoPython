# Decoradores de clase
# Permiten transformar de manera programatica nuestra clase, es similar a los decoradores de fucciones
import inspect


def decorador_repr(cls):
    # print('Se ejecuta decorador de la clase')
    # print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el metodo vars
    atributos = vars(cls)
    # Iteramos cada atributo
    # for nombre, atributo in atributos.items():
    #     if isinstance(atributo, property):
    #         print(f'{nombre}: {atributo}')
    # Revisamos si se ha sobrescrito el metodo __init__
    if '__init__' not in atributos:
        raise TypeError(f'La clase ({cls.__name__}) No ha sobrescrito el metodo __init__')

    firma_init = inspect.signature(cls.__init__)
    # print(f'Firma de __init__: {firma_init}')
    # Recuperamos los parametros exepto el primero
    parametros_init = list(firma_init.parameters)[1:]
    # print(f'Parametros __init__: {parametros_init}')
    # Revisamos si cada parametro tiene un metodo property asociado
    for parametro in parametros_init:
        # property es un valor de typo build-int para preguntar si se esta utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un metodo property para: ({parametro})')

    # Crear el metodo repr dinamicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase de manera dinamica
        nombre_clase = self.__class__.__name__
        # Obtenemos los nombres de las propiedades y sus valores dinamicamente
        # Expresion generadora para crear nombre_atr = valor_atr
        generador_arg = (f'{nombre} = {getattr(self, nombre)!r}' for nombre in parametros_init)
        # Creamos una lista de argumentos
        lista_arg = list(generador_arg)
        # Creamos la cadena apartir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        # Creamos la forma del metodo __repr__, sin su nombre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'

        return resultado_metodo_repr

    # Agregar dinamicamente el metodo repr a nuestra clase
    setattr(cls, '__repr__', metodo_repr)

    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print(f'Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    # def __repr__(self):
    #     return f'Persona({self._nombre}, {self._apellido})'


persona1 = Persona(nombre='Erik', apellido='Towne')
print(persona1)

persona2 = Persona(nombre='Claudio', apellido='Bernier')
print(persona2)
