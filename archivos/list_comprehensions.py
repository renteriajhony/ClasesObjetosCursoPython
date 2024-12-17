
lista = []
lista = [numero for numero in range(6) if numero %2 == 0 and numero%6 ==0]
# print(lista)


lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%3 == 0 else lista_impares.append(numero) for numero in range(6)]
# print(lista_pares)
# print(lista_impares)

lista_listas = [[1,2,3],[4,5,6,7,8,9],[10,11]]
lista_simpe = [valor for sublista in lista_listas for valor in sublista if valor%2==0]
# print(lista_simpe)


