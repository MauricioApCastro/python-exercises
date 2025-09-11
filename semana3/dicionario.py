#cria lista
lista_pessoa = []

# entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

#inclusão na lista em forma de dicionario
pessoa = {"nome": nome, 
        "idade": idade,
        "cidade": cidade }

lista_pessoa.append(pessoa)

print(pessoa)