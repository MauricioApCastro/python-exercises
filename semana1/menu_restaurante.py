print("1 - Hambúrguer (R$ 15,00)")
print("2 - Pizza (R$ 20,00)")
print("3 - Refrigerante (R$ 5,00)")
print("4 - Suco (R$ 7,00)")

opcao = int(input("Escolha uma opção (1-4): "))
if opcao == 1:
    print("Você escolheu Hambúrguer. Preço: R$ 15,00")
elif opcao == 2:
    print("Você escolheu Pizza. Preço: R$ 20,00")
elif opcao == 3:
    print("Você escolheu Refrigerante. Preço: R$ 5,00")
elif opcao == 4:
    print("Você escolheu Suco. Preço: R$ 7,00")
else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
