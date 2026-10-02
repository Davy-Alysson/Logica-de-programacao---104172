import os
os.system('cls')

print("Cardápio")

print("1 - Gta VI / R$ 400,00  ")
print("2 - FC 27 / R$ 350,00")
print("3 - COD: Modern Warfare 4 / R$ 350,00")
print("4 - Gears of War: E-Day / R$ 350,00")
print("5 -  Marvel's Wolverine / R$ 350,00")

um = ("1 - Gta VI / R$ 400,00  ")
dois = ("2 - FC 27 / R$ 350,00")
tres = ("3 - COD: Modern Warfare 4 / R$ 350,00")
quatro = ("4 - Gears of War: E-Day / R$ 350,00")
cinco = ("5 -  Marvel's Wolverine / R$ 350,00")


while True:
    escolha = input(f"Escolha o produto:")

    match escolha:
        case '1':
            print(um)
            break
        case '2':
            print(dois)
            break
        case '3':
            print(tres)
            break
        case '4':
            print(quatro)
            break
        case '5':
            print(cinco)
            break
        case _:
            print("Não existe nada")
            continue
    


