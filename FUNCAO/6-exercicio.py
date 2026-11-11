import os
os.system('cls')


def tabuada(numero):
    print(f"TABUADA DE {numero}")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

numero_usuario = int(input("Digite um número: "))

tabuada(numero_usuario)