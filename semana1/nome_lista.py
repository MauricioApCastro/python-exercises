#inicia uma lista vazia
lista_nomes = []

#pede e armazena 5 nomes na lista
for i in range(1, 6):
    nome = input(f"Digite o nome {i}: ")
    lista_nomes.append(nome)

#pede e armazena nome para busca
nome_procurado = input("Digite um nome para verificar: ")

#verifica se o nome está na lista
if nome_procurado in lista_nomes:
    print(f"O nome {nome_procurado} está na lista")
else:
    print(f"O nome {nome_procurado} não está na lista")
