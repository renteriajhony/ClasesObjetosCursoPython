
# Las funciones en python son ciudadanas de primera clase
# first class citizens

# Definimos la funcion
def sumar(a, b):
    return a + b

# 1- Asignar una funcion a una variable
mi_funcion = sumar
# Verificar el tipo de la variable
print(type(mi_funcion))
# Llamamos la funcion desde la variable
print(mi_funcion(3,5))

# 2 - Pasar funciones como argumentos a una funcion

def operacion(a, b, sumar_arg):
    return f'Resultado desde la funcion sumar como argumento: {sumar_arg(a,b)}'

print(operacion(3,5,sumar))

# Retornar una funcion desde otra funcion
def retornar_funcion():
    return sumar

# Validamos el resultado desde la funcion retornada
mivariable = retornar_funcion()
print(mivariable(4,5))