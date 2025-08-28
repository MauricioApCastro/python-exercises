numeros  = []
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
print(f"O maior número é: {maior}")


#maior = max(numeros)
#print(f"O maior número é: {maior}")

    