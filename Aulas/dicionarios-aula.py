# cria uma lista
estudantes = ["Matheus", 24, "Fernanda", 22]
# mapeando elementos - criando dicionários
estudantes_dic = {'Matheus':24, 'Fernanda':22}
# dicionários sempre com {}
# uma vez criado, podemos usar as chaves do dicionários (os nomes que coloquei ali) como índices 
# é assim que funciona o processo de mapeamento e redução; uma das principais atividades em Big Data
# podemos, ainda, colocar novas chaves automaticamente:
estudantes_dic["Pedro"] = 23
estudantes_dic
print(estudantes_dic)
#limpar dicionário
estudantes_dic.clear()
#deletar
del estudantes_dic
