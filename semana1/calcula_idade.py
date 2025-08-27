from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: ")) 

ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f"Sua idade é: {idade} anos.")