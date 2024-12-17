
# Son fuciones anonimas
# Son funciones pequeñas

# Funcion normal
def sumar(a, b):
    return a+b

# funcion lambda
mi_funcion = lambda a, b: a+b
print(mi_funcion(4, 5))

# Funcion lambda con parametros opcionales
funcion_parametros_opcionales = lambda a=3, b=3: a+b
print(funcion_parametros_opcionales())

# Funcion lambda con argumentos *args y **kwargs
mifuncion_args_kwargs = lambda *args, **kwargs: len(args)+len(kwargs)

print(mifuncion_args_kwargs(1,2,3, name='paul', apellido='Wolker'))

# 