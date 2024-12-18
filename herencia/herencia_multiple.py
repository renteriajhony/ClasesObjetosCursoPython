class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def ordenar(self):
        return self._elementos.sort()

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._elementos!r})'


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos = []):
        super().__init__(elementos)
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()

class ListaEnteros(ListaSimple):
    def __init__(self, elementos = []):
        for elemento in elementos:
            self._validar(elemento)

        super().__init__(elementos)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'El elemento debe ser un numero entero: {elemento}')

    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)

class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass


# Creamos lista de enteros ordenada
listaEnterosOrdenada = ListaEnterosOrdenada([2,3,4,-4,-5])
print(listaEnterosOrdenada)
listaEnterosOrdenada.agregar(-20)
print(listaEnterosOrdenada)