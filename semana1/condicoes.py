#entrada de dados
idade = int(input("Digite sua idade: "))

#processamento
if idade < 18:
    print("Você é menor de idade.")
if idade >= 18 and idade < 60:
    print("Você é adulto.")
if idade >= 60:
    print("Você é idoso.")


