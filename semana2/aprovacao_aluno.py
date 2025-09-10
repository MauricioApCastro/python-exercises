lista_notas = []

nome = input("Qual o seu nome?: ")
qtde_notas =int(input("Quantas notas você vai digitar: "))

for i in range(1,qtde_notas + 1):
    nota = float(input(f"Digite a {i}ª nota: "))
    lista_notas.append(nota)


def calcular_media(lista):

    return sum(lista) / len(lista)

def aprovacao(media):
    if media >= 7 :
        return "Aprovado"
    elif media >= 5:
        return "recuperação"
    else :
        return "reprovado"

def par_impar(lista):   
        pares = [n for n in lista if n % 2 == 0]
        impares = [n for n in lista if n % 2 != 0]
        return pares, impares
     

media = calcular_media(lista_notas)
status = aprovacao(media)
pares, impares = par_impar(lista_notas)

print(f"Nome do aluno: {nome}")
print(f"Suas notas são: {lista_notas}")
print(f"Sua média final é {media}")
print(f"Vocé está {status}")
print(f"A lista de notas pares é {pares} e a ímpares é {impares}")
