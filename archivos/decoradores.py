
# Decoradores: Es una funcion que recibe una funcion y retorna otra
# Nos permiten extender funcionalidades
# 1 Funcion decorador(a)
# 2 Funcion a decorar(b)
# 3 Funcion decorada(c)

# def funcion_decorador_a(funcion_a_decorar_b):
#
#     def funcion_decorada_c(*args, **kwargs):
#         print('Antes de decorar')
#         funcion_a_decorar_b(*args, **kwargs)
#         print('Despues de decorar')
#     return funcion_decorada_c
#
# @funcion_decorador_a
# def mostrar_mensaje():
#     print(f'Hola desde funcion mostrar_mensaje')

# mostrar_mensaje()


def funcion_decorador_a(funcion_a_decorar_b):

    def funcion_decorada_c(*args, **kwargs):
        print('Antes de decorar', *args, **kwargs)
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Despues de decorar')
        return resultado
    return funcion_decorada_c

@funcion_decorador_a
def sumar(a, b):
    return a + b

resultado = sumar(1, 2)
print(resultado)