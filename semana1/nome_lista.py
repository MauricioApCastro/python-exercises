lista_nomes = []

for i in range(1, 6):
    nome = input(f"Digite o nome {i}: ")
    lista_nomes.append(nome)

nome_procurado = input("Digite um nome para verificar: ")

if nome_procurado in lista_nomes:
    print(f"O nome {nome_procurado} está na lista")
else:
    print(f"O nome {nome_procurado} não está na lista")
