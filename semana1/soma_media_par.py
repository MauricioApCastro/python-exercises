lista_numeros = []
lista_pares = []

for i in range(1,6):
   lista_numeros.append(int(input(f"Digite {i} número: ")))

soma = sum(lista_numeros)
media = sum(lista_numeros) / len(lista_numeros)

for numero_par in lista_numeros:
   if numero_par % 2 == 0:
      lista_pares.append(numero_par)
      

print(f"A soma de todos os números é {soma}")

print(f"A media de todos os números é {media}")

print(f"Os números pares são {lista_pares}")
