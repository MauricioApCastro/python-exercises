numero = int(input("Digite um número: "))

for i in range(numero):
    if numero % 1 == 0 and numero % numero == 0:
        print(f"O número {numero} é primo")
        break
else:
    print(f"O número {numero} não é primo")
