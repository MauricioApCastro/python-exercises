numero_secreto = 0
numero_usuario = 1
lista_pares = []
lista_numeros = []

while numero_secreto != numero_usuario:
    numero_usuario = int(input("Digite um número: "))
    if numero_usuario > 1:
        lista_numeros.append(numero_usuario)
    else:
        print("Digite um número positivo!!")


numeros_digitados = len(lista_numeros)
soma = sum(lista_numeros)
media = soma / numeros_digitados

for par in lista_numeros:
    if par % 2 == 0:
        lista_pares.append(par)

print(f"A quantidade de números digitados é: {numeros_digitados}")
print(f"A soma dos números digitados é: {soma}")
print(f"A média dos números é: {media:.2f}")
print(f"A lista dos pares é {lista_pares}")
print("O maior número é", max(lista_numeros) if numeros_digitados > 0 else "nenhum número foi digitado")
print("O menor número é", min(lista_numeros) if numeros_digitados > 0 else "nenhum número foi digitado")

