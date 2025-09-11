import os
import platform
lista_cadastros = [] 

def limpar_tela():

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def cadastrar_pessoa():
    # entrada de dados
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digite sua cidade: ")

    pessoa = {"nome":nome, "idade":idade, "cidade":cidade}






limpar_tela()


print("=== CADASTRO DE PESSOAS ===")
print("1 - Cadastrar pessoa")
print("2 - Ver pessoas cadastradas")
print("3 - Sair")
escolha = int(input("Escolha uma opção: "))

