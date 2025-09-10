


nome = input("Nome do aluno: ")
qtde_notas = int(input("Quantidade de notas: "))

def ler_notas(qtde):
     lista_notas = []

     for i in range(1, qtde + 1):
          while True:
               try:
                    nota = float(input(f"Digite a {i}º nota entre 0 e 10: "))

                    if 0 <= nota <= 10:
                         lista_notas.append(nota)
                         break

                    else:
                          print("❌ Nota fora do intervalo! Digite entre 0 e 10.")

                 
               except ValueError: 
                    print("❌ Entrada inválida! Digite um número.")
          
     return lista_notas



     

def calcular_media(lista):
     media_notas = sum(lista) / len(lista)
     return media_notas
     
def mostrar_status(media):
    if media > 6: situacao = "Aprovado" 
    elif media > 4: situacao = "em Recuperação" 
    else: situacao = "Reprovado"
    return situacao
        



notas = ler_notas(qtde_notas)
media = calcular_media(notas)
status = mostrar_status(media)
     
print(f"Aluno {nome}")
print(f"Notas {notas}")
print(f"Média de notas: {media:.1f}")
print(f"Você está {status}")

