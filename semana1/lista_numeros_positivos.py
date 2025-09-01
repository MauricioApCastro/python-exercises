# inicializa listas e variáveis
lista_numeros = []
numero_usuario = 1  # valor inicial para entrar no while

# coleta números positivos até o usuário digitar 0
while numero_usuario != 0:
    numero_usuario = int(input("Digite um número positivo (0 para sair): "))
    
    if numero_usuario > 0:
        lista_numeros.append(numero_usuario)
    elif numero_usuario < 0:
        print("Digite um número positivo!")

# calcula soma, quantidade e lista de pares após o loop
soma = sum(lista_numeros)
quantidade = len(lista_numeros)
lista_par = [n for n in lista_numeros if n % 2 == 0]

# exibe resultados
print(f"A quantidade de números digitados é: {quantidade}")
print(f"A soma de todos os números é: {soma}")    
print(f"A lista dos números pares é: {lista_par}")  
