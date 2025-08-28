notas_alunos = []
soma = 0

for i in range(5):
    nota_aluno = float(input("Digite a nota {i}"))
    notas_alunos.append(nota_aluno)

for nota_aluno in notas_alunos:
    soma += nota_aluno
    
print(f"A média do aluno é {soma/5}")