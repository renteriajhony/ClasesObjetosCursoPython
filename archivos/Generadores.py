import math


# Generadores
# Es una funcion especial que permite regresar una secuencia de valores.
# Suspende la ejecucion de la funcion yield (producir) (no se usa return)

def generador():
    yield 1
    yield 2
    yield 3

# Consuminos el generadoe a demanda
gen = generador()
# Con cada llamada consuminos un valor
# print(next(gen))
# print(next(gen))
# print(next(gen))
# Si tratamos de consumir mas valores de los que produce el genrador produce error de StopIteration
# print(next(gen))

# Consumiendo los valores del generador desde un ciclo for
# for valor in generador():
#     print(f'Numero generado {valor}')


# #Definimos funcion generador numeros
# def generador_numeros():
#     for numero in range(1,6):
#         yield numero
#         print('Se reanuda la ejecucion de la funcion')
#
# generador = generador_numeros()
# # print(next(generador))
# # print(next(generador))
# # print(next(generador))
#
# for numero in generador:
#     print(numero)


# EXPRESEION GENERADORA
# Es un generador anónimo
multiplicacion = (valor*valor for valor in range(20))
# for mul in multiplicacion:
#     print(mul)
# print(next(multiplicacion))
# print(next(multiplicacion))
# print(next(multiplicacion))

# Tambien se puede pasar una expresion generadora a una funsion (sin parentesis)

suma = sum(multiplicacion)
print(suma)
suma = sum(valor*valor for valor in range(4))
print(suma)

contador = 0
lista = ['Manuel', 'Juan', 'Pablo']
def incrementar():
    global contador
    contador += 1
    return contador

generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = '//\\\\'.join(lista)
print(cadena)