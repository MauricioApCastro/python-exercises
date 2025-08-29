
lista_numeros = []

for i in range (1,6):   
    numero = int(input(f"Digite o {i}º número: "))
    lista_numeros.append(numero)

media = sum(lista_numeros) / len(lista_numeros)

    
print(f"A soma dos números é: {media}")
