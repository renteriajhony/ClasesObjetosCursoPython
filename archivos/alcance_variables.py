
# Alcance de Variables (scope)

variable_global: str = 'Variable Global'

def imprimir():
    global variable_global
    variable_global = 'Variable Global jajaja'
    variable_local = 'Hola'
    print(variable_global)
    print(variable_local)


imprimir()
print(variable_global)