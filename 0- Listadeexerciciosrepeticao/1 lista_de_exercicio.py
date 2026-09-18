import os
os.system("cls")


while True:
    nota = float(input("Digite uma nota:"))
    if 0 <= nota <= 10:
        print(f"Nota valida {nota}")
        break
    else:
        print(f"Nota invalida tente novamente")
