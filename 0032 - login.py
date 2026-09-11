import os
os.system("cls")

nome =  str
senha = str

while True:
    print("PAGINA DE LOGIN")

    print("1 - CADASTRO")
    print("2 - LOGIN")
    print("3 - FIM")

    escolha = input("Escolha um opcao:")

    if escolha == "1":
        print("Cadastro")

        nomec = str(input('Digite seu nome:'))
        senhac = str(input("Digite uma senha:"))

    elif escolha == "2":
        print("Login")

        nomel = input('Digite seu nome:')
        senhal = input('Digite sua senha:')
        
        if nomel == nomec and senhal == senhac:
            print("Logado")
            
        else:
            print("Nome ou senha errado")
            
    elif escolha == "3":
        print('PROGRAMA FINALIZADO')

        break

    