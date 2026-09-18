import os

os.system("cls")

while True:
    print("CARDAPIO")

    print("1 - Picanha")
    print("2 - Lasanha")
    print("3 - Strogonoff")
    print("4 - Bife acebolado")
    print("5 - Pao com ovo")

    escolha = input("Digite o codigo:")

    match escolha:
        case "1":
            print("Picanha -> R$ 25,00")
            
        case "2":
            print("Lasanha -> R$ 20,00")
            
        case "3":
            print("Strogonoff -> R$ 18,00")
            
        case "4":
            print("Bife acebolado -> R$ 15,00")
            
        case "5":
            print("Pao com ovo -> R$ 5,00")
        case _:
            print("CODIGO INVALIDO")
            