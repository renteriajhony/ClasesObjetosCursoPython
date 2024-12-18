# Ejemplo atributos publicos, protejidos, privados
class MiClase:
    def __init__(self, publico, protejido, privado):
        self.publico = publico
        self._protejido = protejido
        self.__privado = privado