lista_produtos = []
qtde_produtos = int(input("Quantos produtos você vai cadastrar?: "))

for i in range(1, qtde_produtos + 1):
    print(f"Dados do produto {i}")
    nome_produto = input("Nome: ")
    preco_produto = float(input("Preço: "))
    produto = {"nome": nome_produto, "preco": preco_produto}
    lista_produtos.append(produto)

def total_gasto(lista):    
    return sum(produto["preco"] for produto in lista)
    
def maior_menor(lista):
    mais_barato = min(produto["preco"] for produto in lista)
    mais_caro = max(produto["preco"] for produto in lista)
    return mais_barato, mais_caro

def media_produtos(lista):
    return total_gasto(lista) / len(lista)

# chamadas
total = total_gasto(lista_produtos)
media = media_produtos(lista_produtos)
barato, caro = maior_menor(lista_produtos)

# saída
print(f"\nVocê cadastrou {qtde_produtos} produtos")
print(f"O total gasto foi R${total:.2f}")
print(f"A média de gasto foi R${media:.2f}")
print(f"O produto mais caro custa R${caro:.2f} e o mais barato custa R${barato:.2f}")
