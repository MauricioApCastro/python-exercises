import os

# Lista para armazenar os números
lista_numeros = []

# Loop até ter 10 números positivos
while len(lista_numeros) < 10:
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa o terminal a cada entrada
    try:
        numero = int(input(f"Digite o {len(lista_numeros)+1}º número positivo: "))
        if numero > 0:
            lista_numeros.append(numero)
        else:
            print("⚠️ Número inválido! Digite um número positivo.")
    except ValueError:
        print("⚠️ Entrada inválida! Digite apenas números inteiros.")

# Cálculos
quantidade = len(lista_numeros)
soma = sum(lista_numeros)
media = soma / quantidade
maior = max(lista_numeros)
menor = min(lista_numeros)

# Listas de pares e ímpares
lista_pares = [n for n in lista_numeros if n % 2 == 0]
lista_impares = [n for n in lista_numeros if n % 2 != 0]

# Resultados
print("\n--- Resultados ---")
print(f"Lista completa: {lista_numeros}")
print(f"Quantidade: {quantidade}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Pares: {lista_pares}")
print(f"Ímpares: {lista_impares}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
