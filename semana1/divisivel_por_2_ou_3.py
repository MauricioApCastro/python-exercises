numero = int(input("Digite um número: "))

if (numero % 2 == 0) and (numero % 3 == 0):
    print("é divisível por 2 e 3")
elif (numero % 2 == 0):
    print("é divisível por 2")
elif (numero % 3 == 0):
    print("é divisível por 3")
else:
    print("não é divisível por nenhum dos dois")
    