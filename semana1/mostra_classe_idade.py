idade = int(input("Digite sua idade: "))
if idade < 12:
    print("Você é uma criança.")
elif 12 <= idade < 18:
    print("Você é um adolescente.")
elif 18 <= idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")