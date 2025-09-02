lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i} º número positivo:"))

    if numero < 0 :
        print("⚠️ Número inválido! Digite um número positivo.")
        i = i-1

    else:
        lista_numeros.append(numero)

quantidade = len(lista_numeros)
soma = sum(lista_numeros)
media = soma / quantidade
maior = max(lista_numeros)
menor = min(lista_numeros)

for n in lista_numeros:
    if n % 2 == 0:
        lista_pares.append(n)

for n in lista_numeros:
    if n % 2 != 0:
        lista_impares.append(n)



print(f"Lista completa: {lista_numeros}")
print(f"Quantidade: {quantidade}")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Pares: {lista_pares}")
print(f"Pares: {lista_impares}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")    