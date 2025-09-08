lista_notas = []

qtde_alunos = int(input("Quantidade de alunos: "))

for i in range(1, qtde_alunos + 1):
    nome = input("Nome do aluno: ")

    notas_trimestre = []

    for j in range(1, 4):
        nota = float(input(f"Digite a nota do {j}º trimestre: "))
        notas_trimestre.append(nota)
    
notas_aluno = {"nome": nome, "notas": notas_trimestre}
lista_notas.append(notas_aluno)