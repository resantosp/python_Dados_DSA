#Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

f1 = input('Informe a primeira fruta: ').title()
f2 = input('Informe a primeira fruta: ').title()
f3 = input('Informe a primeira fruta: ').title()
f4 = input('Informe a primeira fruta: ').title()
f5 = input('Informe a primeira fruta: ').title()

lista = [f1, f2, f3, f4, f5]

if 'Morango' in lista:
    print('\nHmmm. No momento não há a fruta Morango disponível.')
else:
    print('\nTudo certo. Sua compra chegará em breve.')
