nome = input("Qual o seu nome? :")
idade = int(input("Qual a sua idade? :"))
altura = float(input("Qual a sua altura :"))
peso = float(input("Qual o seu peso? :"))

imc = peso / altura ** 2

if(imc < 18.5):
   res = "abaixo do peso"
elif(18.5 and 24.9):
   res = "Peso normal"
elif(25 and 29.9):
   res = "Sobrepeso"
else:
   res = "Sobrepeso"

print(f"Olá {nome}, você tem {idade} anos e mede {altura:.2f}m, pesa {peso} e seu IMC é {imc:.2f}") 
print(res)