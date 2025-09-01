numero_secreto = 0
numero = -1  # qualquer valor diferente de numero_secreto

while numero != numero_secreto:
    numero = int(input("Adivinhe o número: "))
    if numero != numero_secreto:
        print("Muito alto" if numero > numero_secreto else "Muito baixo")

print("Parabéns você acertou!!")
