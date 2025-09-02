numero_secreto = 5
lista_palpites = []
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número!: "))

    lista_palpites.append(palpite)


    if palpite < numero_secreto:
        print("Muito baixo")
    elif palpite > numero_secreto:
        print("Muito alto")
    else:
        print(f"Parabéns, você acertou o número secreto {numero_secreto}!")
        break
    tentativas += 1

tentativas = len(lista_palpites)

print(f"Você precisou de {tentativas} tentativas")
print(f"Seus palpites foram: {lista_palpites}")
