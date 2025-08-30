num = int(input("Digite um número: "))

if num > 1 and all(num % i != 0 for i in range(2, num)):
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")
