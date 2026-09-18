import os
os.system("cls")

while True:
    nome_usuario = input("Digite seu usuario:")
    senha = input("Digite sua senha:")

    if nome_usuario == senha:
        print("Login invalido")
        print("Tente novamente")
    else:
        print("Login valido")
        break