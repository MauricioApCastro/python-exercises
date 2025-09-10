lista_notas = []

qtde_alunos = int(input("Quantidade de alunos: "))

for i in range(1, qtde_alunos + 1):
    nome = input(f"Nome do {i}º aluno: ")

    notas_trimestre = []

    for j in range(1, 4):
        nota = float(input(f"Digite a nota do {j}º trimestre: "))
        notas_trimestre.append(nota)
    
    notas_aluno = {"nome": nome, "notas": notas_trimestre}
    lista_notas.append(notas_aluno)


def calcular_medias(lista):
    for aluno in lista:
        nome = aluno["nome"]
        notas = aluno["notas"]

        media_aluno = sum(notas) / len(notas)

    return media_aluno



media = calcular_medias(lista_notas)

print(f"O aluno {"nome"} obteve a média de {"notas"}")