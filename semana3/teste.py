
import random

numero_secreto = random.randint(1,10)
palpite = None
contador = 0

while numero_secreto != palpite:
    palpite = int(input("Adivinhe o número: "))
    if palpite > numero_secreto: 
        print("Muito alto!")
    elif palpite < numero_secreto:
        print("Muito baixo")
    else:
       print("Parabéns você acertou!")
       
    contador = contador + 1

print(f"Acertou com {contador} tentativas!!")




