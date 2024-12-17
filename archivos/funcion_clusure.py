
# Son funciones que encapsulan a otras funciones, pero mantienen un estado y ademas la puede regresar
# La funcion anidada puede acceder a las variables locales definidas en la funcion principal o externa

def operacion(a, b):
    # Definimos funcion interna
    # def sumar():
    #     return a + b

    return lambda : a+b

variable = operacion(1, 2)
print(variable())

print(operacion(1, 2)())