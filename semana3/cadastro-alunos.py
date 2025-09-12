import os
import platform

lista_cadastros = []

# Função para limpar a tela
def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Função cadastrar pessoa
def cadastrar_pessoa():
    nome = input("Digite seu nome: ")
    
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("❌ Digite um número válido para a idade!")
    
    cidade = input("Digite sua cidade: ")

    pessoa = {"nome": nome, "idade": idade, "cidade": cidade}
    lista_cadastros.append(pessoa)
    print("\n✅ Pessoa cadastrada com sucesso!")
    input("\nPressione ENTER para continuar...")

# Função mostrar cadastros
def mostrar_cadastros():
    if not lista_cadastros:
        print("\n⚠ Nenhuma pessoa cadastrada.")
    else:
        print("\n=== Pessoas Cadastradas ===")
        for i, pessoa in enumerate(lista_cadastros, start=1):
            print(f"{i} - Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
    input("\nPressione ENTER para continuar...")

# Função buscar pessoa
def buscar_pessoa(nome_procurado):
    encontrado = False
    for pessoa in lista_cadastros:
        if pessoa["nome"].lower() == nome_procurado.lower():
            print(f"\n✅ Encontrado: Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
            encontrado = True
            break
    if not encontrado:
        print("\n❌ Pessoa não encontrada.")
    input("\nPressione ENTER para continuar...")

# Função excluir pessoa
def excluir_pessoa(nome_procurado):
    for pessoa in lista_cadastros:
        if pessoa["nome"].lower() == nome_procurado.lower():
            lista_cadastros.remove(pessoa)
            print("\n✅ Pessoa excluída!")
            break
    else:
        print("\n❌ Pessoa não encontrada.")
    input("\nPressione ENTER para continuar...")

# Loop do menu
while True:
    limpar_tela()
    print("=== CADASTRO DE PESSOAS ===")
    print("1 - Cadastrar pessoa")
    print("2 - Ver pessoas cadastradas")
    print("3 - Buscar pessoa")
    print("4 - Excluir pessoa")
    print("5 - Sair")

    try:
        escolha = int(input("\nEscolha uma opção: "))
        if escolha == 1:
            cadastrar_pessoa()
        elif escolha == 2:
            mostrar_cadastros()
        elif escolha == 3:
            nome_procurado = input("Busca por nome: ").strip()
            buscar_pessoa(nome_procurado)
        elif escolha == 4:
            nome_procurado = input("Nome para excluir: ")
            excluir_pessoa(nome_procurado)
        elif escolha == 5:
            print("\nSaindo...")
            break
        else:
            print("\n❌ Opção inválida, escolha de 1 a 5.")
            input("\nPressione ENTER para continuar...")
    except ValueError:
        print("\n❌ Entrada inválida! Digite um número.")
        input("\nPressione ENTER para continuar...")
