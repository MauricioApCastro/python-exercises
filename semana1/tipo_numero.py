numero = int(input("Digite um número: "))

if numero > 0:
    tipo = "positivo"

elif numero < 0:
    tipo = "negativo"

else:
    tipo = "zero"

print(f"O número é {tipo}")