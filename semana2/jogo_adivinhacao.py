numero_secreto = 5
palpite = 1
lista_palpites = []

while numero_secreto != palpite:
    palpite = int(input("Adivinhe o número!: "))

    lista_palpites.append(palpite)


    if palpite < numero_secreto:
        print("Muito baixo")
    elif palpite > numero_secreto:
        print("Muito alto")
    else:
        print("Parabéns você acertou!")

tentativas = len(lista_palpites)

print(f"Tentativas: {tentativas}")
print(f"Números tentados: {lista_palpites}")
