#Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

import unicodedata

dia = input('Que dia é hoje? ').lower().strip()

dia = unicodedata.normalize("NFD", dia)
dia = dia.encode("ascii", "ignore")
dia = dia.decode("utf-8")

if dia == "domingo" or dia == "sabado":
    print('Hoje é dia de descanso!')
else:
    print("Você precisa trabalhar!")
