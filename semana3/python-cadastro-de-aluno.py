lista_notas = []

qtde_alunos = int(input("Quantos alunos você vai cadastrar?: "))

for i in range(1, qtde_alunos + 1):
    nome = input(f"Qual o nome do {i}º aluno?: ")

    # cria uma lista de notas só para este aluno
    notas_trimestre = []  

    for j in range(1, 4):
        nota = float(input(f"Digite a nota do {j}º trimestre: "))
        notas_trimestre.append(nota)

    # monta o dicionário do aluno
    notas_aluno = {"nome": nome, "notas": notas_trimestre}
    lista_notas.append(notas_aluno)

    def media(lista):
        return lista_notas(lista) / len(lista)


    print(f"A média do aluno é: {media}")