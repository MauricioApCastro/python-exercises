#inicia uma lista vazia
lista_numeros = []
lista_quadrados = []

for i in range(1,5):
    numero = int(input(f"Digite o {i} número: "))
    lista_numeros.append(numero)

lista_quadrados = [n ** 2 for n in lista_numeros]



print(f"A lista dos quadrados dos números é : {lista_quadrados}")



    