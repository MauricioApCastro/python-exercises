import os
import platform

# Lista principal que armazenará todos os alunos
lista_cadastro = []

# Função para limpar a tela
def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Função para cadastrar um aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    
    while True:
        try:
            idade = int(input("Digite a idade: "))
            break
        except ValueError:
            print("❌ Digite um número válido para a idade!")
    
    cidade = input("Digite a cidade: ")
    
    # Cria o dicionário do aluno com lista de notas vazia
    aluno = {"nome": nome, "idade": idade, "cidade": cidade, "notas": []}
    lista_cadastro.append(aluno)
    print("\n✅ Aluno cadastrado com sucesso!")
    input("\nPressione ENTER para continuar...")

# Função para cadastrar notas de um aluno
def cadastrar_notas():
    if not lista_cadastro:
        print("\n⚠ Nenhum aluno cadastrado.")
        input("\nPressione ENTER para continuar...")
        return
    
    nome_busca = input("Digite o nome do aluno para cadastrar notas: ").strip()
    for aluno in lista_cadastro:
        if aluno["nome"].lower() == nome_busca.lower():
            while True:
                try:
                    nota = float(input("Digite a nota entre 0 e 10: "))
                    if 0 <= nota <= 10:
                        aluno["notas"].append(nota)
                        print("✅ Nota cadastrada!")
                        break
                    else:
                        print("❌ Nota fora do intervalo! Digite entre 0 e 10.")
                except ValueError:
                    print("❌ Entrada inválida! Digite um número.")
            break
    else:
        print("❌ Aluno não encontrado.")
    
    input("\nPressione ENTER para continuar...")

# Função para calcular a média de um aluno
def calcular_media_aluno(aluno):
    if aluno["notas"]:
        return sum(aluno["notas"]) / len(aluno["notas"])
    else:
        return None

# Função para mostrar todos os alunos e suas médias
def mostrar_alunos_e_medias():
    if not lista_cadastro:
        print("\n⚠ Nenhum aluno cadastrado.")
    else:
        print("\n=== Alunos e Médias ===")
        for i, aluno in enumerate(lista_cadastro, start=1):
            media = calcular_media_aluno(aluno)
            if media is not None:
                print(f"{i} - Nome: {aluno['nome']}, Média: {media:.1f}")
            else:
                print(f"{i} - Nome: {aluno['nome']}, Média: Sem notas")
    input("\nPressione ENTER para continuar...")

# Função para buscar um aluno pelo nome
def buscar_aluno():
    if not lista_cadastro:
        print("\n⚠ Nenhum aluno cadastrado.")
        input("\nPressione ENTER para continuar...")
        return
    
    nome_busca = input("Digite o nome do aluno para buscar: ").strip()
    for aluno in lista_cadastro:
        if aluno["nome"].lower() == nome_busca.lower():
            print(f"\n✅ Encontrado: Nome: {aluno['nome']}, Idade: {aluno['idade']}, Cidade: {aluno['cidade']}")
            if aluno["notas"]:
                print(f"Notas: {aluno['notas']}")
                print(f"Média: {calcular_media_aluno(aluno):.1f}")
            else:
                print("Sem notas cadastradas.")
            break
    else:
        print("❌ Aluno não encontrado.")
    
    input("\nPressione ENTER para continuar...")

# Função para excluir um aluno pelo nome
def excluir_aluno():
    if not lista_cadastro:
        print("\n⚠ Nenhum aluno cadastrado.")
        input("\nPressione ENTER para continuar...")
        return
    
    nome_busca = input("Digite o nome do aluno para excluir: ").strip()
    for aluno in lista_cadastro:
        if aluno["nome"].lower() == nome_busca.lower():
            lista_cadastro.remove(aluno)
            print("\n✅ Aluno excluído!")
            break
    else:
        print("❌ Aluno não encontrado.")
    
    input("\nPressione ENTER para continuar...")

# Loop principal do menu
while True:
    limpar_tela()
    print("=== SISTEMA DE CADASTRO DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Cadastrar notas")
    print("3 - Ver alunos e médias")
    print("4 - Buscar aluno")
    print("5 - Excluir aluno")
    print("6 - Sair")
    
    try:
        escolha = int(input("\nEscolha uma opção: "))
        if escolha == 1:
            cadastrar_aluno()
        elif escolha == 2:
            cadastrar_notas()
        elif escolha == 3:
            mostrar_alunos_e_medias()
        elif escolha == 4:
            buscar_aluno()
        elif escolha == 5:
            excluir_aluno()
        elif escolha == 6:
            print("\nSaindo do sistema...")
            break
        else:
            print("\n❌ Opção inválida. Escolha de 1 a 6.")
            input("\nPressione ENTER para continuar...")
    except ValueError:
        print("\n❌ Entrada inválida! Digite um número.")
        input("\nPressione ENTER para continuar...")
