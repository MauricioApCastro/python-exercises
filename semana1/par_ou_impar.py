numero = int(input("Digite um número: "))

if numero > 0:
    sinal = "positivo"
    if numero % 2 == 0 :
        posicao = "par"
    else:
        posicao = "impar"


if numero < 0:
    sinal = "negativo"
    if numero % 2 == 0 :
        posicao = "par"
    else:
        posicao = "impar"

if numero == 0:
    sinal = ""
    posicao = "é zero"


    
print(f"o número é {sinal} e {posicao}")