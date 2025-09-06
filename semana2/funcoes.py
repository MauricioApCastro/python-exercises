import os

lista_numeros = []

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



def estatistica(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = soma / quantidade
    maior = max(lista)
    menor = min(lista)
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    return quantidade, soma, media, maior, menor, pares, impares

qtd, soma, media, maior, menor, pares, impares = estatistica(lista_numeros)

# Resultados
print("\n--- Resultados ---")
print(f"Lista completa: {lista_numeros}")
print(f"Quantidade: {qtd}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")





