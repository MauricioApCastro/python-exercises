lista_numeros = []

for i in range(1,6):
    nomes = int(input("Digite um número: "))
    lista_numeros.append(nomes)


maior = lista_numeros[0]
menor = lista_numeros[0]

for numero in lista_numeros:
    if numero > maior:
        maior = numero

for numero in lista_numeros:
    if numero < menor:
        menor = numero
        
soma = 0
for numero in lista_numeros:
    soma = soma + numero

print(lista_numeros)
print(f"O menor é {menor} e o maior é {maior}")
print(f"A soma de todos os número é {soma}")
