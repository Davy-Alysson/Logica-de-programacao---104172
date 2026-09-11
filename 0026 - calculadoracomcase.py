import os

os.system("cls")

while True:
    print("+ -> SOMA")
    print("- -> SUBTRACAO")
    print("* -> MULTIPLICACAO")
    print("/ -> DIVISAO")

    primeiro_numero = float(input("Digite o primeiro numero:"))
    operador = input("Digite a operacao:")
    segundo_numero = float(input("Digite o segundo numero:"))

    match operador:
        case "+":
            print("Soma =", (primeiro_numero + segundo_numero))
        case "-":
            print("Subtracao =", (primeiro_numero - segundo_numero))
        case "*":
            print("Multiplicacao =", (primeiro_numero * segundo_numero))
        case "/":
            print("Divisao =", (primeiro_numero / segundo_numero))
        case _:
            print("OPERADOR ESCOLHIDO INVALIDO")

