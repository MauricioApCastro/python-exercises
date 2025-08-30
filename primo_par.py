lista_resultado = []
num = int(input("Digite um número: "))

for i in range(1, num + 1):   # percorre de 1 até o número
    res = (num % i == 0)      # True se for divisor
    lista_resultado.append(res)

# Um número primo só tem 2 divisores: 1 e ele mesmo
if lista_resultado.count(True) == 2:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")

print(lista_resultado)  # só para você ver como fica a lista


