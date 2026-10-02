import os
import time
os.system('cls')


print('LOGIN')

loginc = str(input("Crie um nome:"))
senhac = int(input("Crie sua senha:"))
os.system('cls')

while True:
    login = str(input("Digite seu login:"))
    senha = int(input("Digite sua senha:"))
    if login == loginc and senha == senhac:
        print("Credenciais corretas")
        break
    else:
        print("Suas credenciais estão incorretas")
        input("Pressione qualquer botão para tentar novamente")
        time.sleep(1)
        os.system('cls')
    

    