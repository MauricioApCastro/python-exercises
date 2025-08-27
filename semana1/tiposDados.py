nome = input("Qual é o seu nome? ")
idade =int( input("Qual é a sua idade? "))
altura = float(input("Qual é a sua altura? "))
gosta_de_python = input("Você gosta de Python? (true/false) ").strip().lower() == 'true'

print(f"Olá, {nome}!")
print(f"Você tem {idade}, mede {altura} e gosta de Python?{gosta_de_python}")



