import os
import platform
lista_cadastros = [] 

#funçao para limpar a tela
def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def cadastrar_pessoa():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digite sua cidade: ")

    pessoa = {"nome": nome, "idade": idade, "cidade": cidade}
    lista_cadastros.append(pessoa)
    print("\n✅ Pessoa cadastrada com sucesso!")
    input("\nPressione ENTER para continuar...")

def mostrar_cadastros():
    if not lista_cadastros:
        print("\n⚠ Nenhuma pessoa cadastrada.")
    else:
        print("\n=== Pessoas Cadastradas ===")
        for i, pessoa in enumerate(lista_cadastros, start=1):
            print(f"{i} - Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
    input("\nPressione ENTER para continuar...")

while True:
    limpar_tela()
    print("=== CADASTRO DE PESSOAS ===")
    print("1 - Cadastrar pessoa")
    print("2 - Ver pessoas cadastradas")
    print("3 - Sair")
    
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            cadastrar_pessoa()
        elif escolha == 2:
            mostrar_cadastros()
        elif escolha == 3:
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida, escolha 1, 2 ou 3.")
            input("\nPressione ENTER para continuar...")
    except ValueError:
        print("❌ Entrada inválida! Digite um número.")
        input("\nPressione ENTER para continuar...")
