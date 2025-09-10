import os
import platform

# -------- Funções utilitárias --------
def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# -------- Funções principais --------
def ler_notas():
    lista_notas = []
    qtde_notas = int(input("Quantas notas deseja digitar? "))

    for i in range(1, qtde_notas + 1):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota entre 0 e 10: "))
                if 0 <= nota <= 10:
                    lista_notas.append(nota)
                    break
                else:
                    print("❌ Nota fora do intervalo! Digite entre 0 e 10.")
            except ValueError:
                print("❌ Entrada inválida! Digite um número.")
    return lista_notas

def calcular_media(lista):
    return sum(lista) / len(lista)

def mostrar_status(media):
    if media > 6:
        return "Aprovado"
    elif media > 4:
        return "em Recuperação"
    else:
        return "Reprovado"
    




# -------- Programa principal --------
notas = []
nome = input("Nome do aluno: ")

while True:
    limpar_tela()

    print("=== MENU PRINCIPAL ===")
    print("1 - Digitar notas")
    print("2 - Calcular médias")
    print("3 - Sair")

    try:
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            notas = ler_notas()
            input("\n✅ Notas salvas! Pressione ENTER para continuar...")

        elif escolha == 2:
            if len(notas) == 0:
                print("❌ Nenhuma nota cadastrada!")
            else:
                media = calcular_media(notas)
                status = mostrar_status(media)
                print(f"\nAluno: {nome}")
                print(f"Notas: {notas}")
                print(f"Média: {media:.1f}")
                print(f"Status: {status}")
            input("\nPressione ENTER para continuar...")

        elif escolha == 3:
            print("Saindo...")
            break

        else:
            print("❌ Opção inválida, escolha 1, 2 ou 3.")
            input("\nPressione ENTER para continuar...")

    except ValueError:
        print("❌ Entrada inválida! Digite um número.")
        input("\nPressione ENTER para continuar...")
