import os
os.system("cls")

print("Soma +")
print("Subtração -")
print("Multiplicação x")
print("Divisão /")


operacao = input("Digite a operação:")
numero = int(input("Digite o número:"))

match operacao:
    case "+":
        for i in range(1,11):
            print(f"{numero} + {i} = {numero + i}")
    case "-":
        for i in range(1,11):
            print(f"{numero} - {i} = {numero - i}")
    case "x":
        for i in range(1,11):
            print(f"{numero} x {i} = {numero * i}")
    case "/":
        for i in range(1,11):
            print(f"{numero} / {i} = {numero / 1:.2f}")

    