lista_notas = []

nome = input("Qual o seu nome?: ")
qtde_notas =int(input("Quantas notas você vai digitar: "))

for i in range(1,qtde_notas + 1):
    nota = float(input(f"Digite a {1} nota: "))
    lista_notas.append(nota)


def calcular_media(lista):

    return
    sum(lista_notas) / len(lista_notas)

media = calcular_media(lista_notas)


print(f"Nome do aluno {nome}")
print(f"Suas notas são: {media:.2f}")
print(f"Sua média final é {media}")
