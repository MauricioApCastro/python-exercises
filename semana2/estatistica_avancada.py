import os

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) e classifica o resultado.

    Parâmetros:
        peso (float): Peso da pessoa em kg.
        altura (float): Altura da pessoa em metros.

    Retorna:
        tuple: Contendo os seguintes valores:
            - imc (float): Valor do índice IMC.
            - classificacao (str): Classificação do IMC conforme a OMS.
    """
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return imc, classificacao


# --- Programa Principal ---
os.system('cls' if os.name == 'nt' else 'clear')

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Entrada com validação
while True:
    try:
        peso = float(input("Digite seu peso (kg): "))
        if peso <= 0:
            print("⚠️ Peso inválido! Digite um valor maior que 0.")
            continue
        break
    except ValueError:
        print("⚠️ Entrada inválida! Digite apenas números.")

while True:
    try:
        altura = float(input("Digite sua altura (m): "))
        if altura <= 0:
            print("⚠️ Altura inválida! Digite um valor maior que 0.")
            continue
        break
    except ValueError:
        print("⚠️ Entrada inválida! Digite apenas números.")

imc, classificacao = calcular_imc(peso, altura)

# --- Resultados ---
print("\n--- Resultado ---")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} m")
print(f"Peso: {peso:.1f} kg")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
