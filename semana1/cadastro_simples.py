nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))  
gosta_python = input("Você gosta de Python? (true/false): ").strip().lower()== 'true'

print("\n--- Dados Cadastrados ---")
print(f"Nome: {nome}")  
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} metros")
print(f"Gosta de Python: {gosta_python}")