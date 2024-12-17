
# Funciones anidadas
def calculadora(a, b):
    # Funcion anidada
    def sumar(a, b):
        return a + b
    def multiplicacion(a, b):
        return a * b
    def division(a, b):
        return a / b
    def restante(a, b):
        return a - b

    #Llamada a funcion anidada
    print(sumar(a, b))
    print(multiplicacion(a, b))
    print(division(a, b))
    print(restante(a, b))


print(calculadora(100,2))