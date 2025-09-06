lista_numeros = []

for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    lista_numeros.append(numero)

def estatistica(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

res_soma, res_media = estatistica(lista_numeros)
print(f"A soma é: {res_soma}")
print(f"A média é: {res_media}")
