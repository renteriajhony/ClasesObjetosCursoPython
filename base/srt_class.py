import string

# nombre = 'Jhony'
# edad = 34
# sueldo = 5000
#
# def getName():
#     return nombre
#
# mensaje = f'Nombre {getName()*5}'
# print(mensaje)
#
# print(nombre, edad, sueldo, sep='')


# mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre.upper(), edad, sueldo)
# # print(mensaje)
#
# mensaje = 'Nombre {0} Edad {1} Sueldo {2:.3f}'.format(nombre.upper(), edad, sueldo)
# # print(mensaje)
#
# mensaje = 'Nombre {n} Edad {e} Sueldo {s}'.format(n=nombre.upper(), e=edad, s=sueldo)
# # print(mensaje)
#
# diccionario = {'nombre': 'Juan', 'edad': 30, 'sueldo': 5000}
# mensaje = 'Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]}'.format(persona=diccionario)
# # print(mensaje)

# mensaje = b'hola mundo'
# print(mensaje[0])
# print(chr(104))
#
# mensaje = b'hola mundo'.split()
# print(mensaje)


string = 'Programación con Python'
print('Cadena original:', string)

bytes = string.encode('utf-8')
print('Cadena bytes:', bytes)