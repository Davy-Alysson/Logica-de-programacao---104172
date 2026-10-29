import os
os.system('cls')

lista = []

while True:

    print("SÉRIES DENDEZEIROS")
    print("1 - GUARDAR SÉRIE")
    print("2 - LISTAR SÉRIES")
    print("0 - SAIR")

    opcao = int(input("Escolha: "))

    match opcao:
        case 1:
            