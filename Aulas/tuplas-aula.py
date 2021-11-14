# em python, tuplas são mto semelhantes às listas, mas são IMUTÁVEIS

# exemplo de uso: para representar dados que n devem ser alterados, como os dias da semana ou datas em um calendário

# são construídas com o uso de parênteses () e vírgulas separando cada elemento da tupla

tupla = ('item1', 'item2', 'item3')

# se no programa vc precisa ter CERTEZA de que os dados NÃO SOFRERÃO mudanças, então tuplas podem ser a solução

# Então...

#listas = []
#dicionários = {}
#tuplas = ()

#usando a função list() para converter uma tupla para lista
t2 = ('A', 'B', 'C')
lista_tupla = list(t2)
print(lista_tupla)

#vamos colocar agr um item a mais na lista
lista_tupla.append('D')
print(lista_tupla)

#agora reconvertendo...
t2 = tuple(lista_tupla)
print(t2)
