idade = int(input("Qual a sua idade?"))

if idade < 11:
    estado = "criança"

elif idade < 17:
    estado = "adolescente"

else:
    estado = "adulto"

print(f"Você é {estado}")
