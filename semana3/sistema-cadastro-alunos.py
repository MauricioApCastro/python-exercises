import os
import platform

lista_cadastro = []

# Função para limpar a tela
def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("❌ Digite um número válido para a idade!")
    
    cidade = input("Digite sua cidade: ")
    

    aluno = {"nome": nome, "idade": idade, "cidade": cidade, "notas": []}
    lista_cadastro.append(aluno)
    print("\n✅ Pessoa cadastrada com sucesso!")
    input("\nPressione ENTER para continuar...")





    

while True:
    limpar_tela()
    print("=== SISTEMA DE CADASTRO DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Cadastrar notas")
    print("3 - Ver alunos e médias")
    print("4 - Buscar aluno")
    print("5 - Sair")

    try:
        escolha = int(input("\nEscolha uma opção: "))
        if escolha == 1:
           cadastrar_aluno()
        elif escolha == 2:
            nome_busca = "Escolha o aluno para cadastrar notas:"
            #"cadastrar_notas()
        elif escolha == 3:
            nome_procurado = input("Busca por nome: ").strip()
            #Ver alunos e médias
        elif escolha == 4:
            nome_procurado = input("Nome para excluir: ")
            #Buscar aluno
        elif escolha == 5:
            print("\nSaindo...")
            break
        else:
            print("\n❌ Opção inválida, escolha de 1 a 5.")
            input("\nPressione ENTER para continuar...")
    except ValueError:
        print("\n❌ Entrada inválida! Digite um número.")
        input("\nPressione ENTER para continuar...")
