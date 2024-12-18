class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        return self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._elementos!r})'


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos = []):
        super().__init__(elementos)
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        self.ordenar()

class ListaEnteros(ListaSimple):
    def __init__(self, elementos = []):
        for elemento in elementos:
            self._validar(elemento)

        super().__init__(elementos)
        self._elementos = elementos

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'El elemento debe ser un numero entero: {elemento}')

    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)
        self.ordenar()

# Creacion de lista simpre
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)
# Creacion de lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))
# Creacion de lista de enteros
lista_enteros = ListaEnteros([4,2,3])
print(lista_enteros)
lista_enteros.agregar(5.3)
print(lista_enteros)