import os
os.system("cls")

while True:

    dia = int(input("Digite um numero entre 1 e 7:"))

    match dia:
        case "1":
            print("DOMINGO")
        case "2":
            print("SEGUNDA")
        case "3":
            print("TERCA")
        case "4":
            print("QUARTA")
        case "5":
            print("QUINTA")
        case "6":
            print("SEXTA")
        case "7":
            print("SABADO")
        case _:
            print("DIA INVALIDO")