lista_numeros = []

for i in range(1, 6):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

maior = max(lista_numeros)   # maior valor da lista
menor = min(lista_numeros)   # menor valor da lista
soma = sum(lista_numeros)    # soma de todos os valores

print(lista_numeros)
print(f"O menor é {menor} e o maior é {maior}")
print(f"A soma de todos os números é {soma}")
