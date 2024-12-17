from base64 import decode

variable = 1,2,'j',4,5,6,7
print(variable)
print(type(variable))


_,_ , *z = variable
print(z)
print(_)



tupla = (1,2,3,7)
lista = [4,5,6,7]
diccionario = {'7':7,'8':8,'9':9}
print(type(tupla))
print(type(lista))
print(type(diccionario))

mezcla = zip(tupla,lista)
print(dict(mezcla))