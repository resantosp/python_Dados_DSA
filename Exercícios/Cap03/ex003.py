# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista

tupla = ('a', 'b', 'c', 'd')
lista = []

for i in tupla:
    lista = lista + [i * 2]
    
print(lista)
