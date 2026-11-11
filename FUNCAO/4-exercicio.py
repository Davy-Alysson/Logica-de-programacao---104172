import os
os.system('cls')

def logo_senai():
    print('='*15)
    print(' SENAI - BAHIA')
    print('='*15)

def menu():
    print('1 - CADASTRAR ALUNO')
    print('2 - MOSTRAR DADOS DO ALUNO')
    print('3 - SAIR')

def mostrar_dados(nome, email, tel):
    try:
        print(f"Nome: {nome}\nEmail: {email}\nTelefone: {tel}")
    except:
        print("Nenhum dado cadastrado.")

while True:
    logo_senai()
    menu()
    escolha = input('Escolha: ')


    match escolha:
        case "1":
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            tel = input("Digite seu telefone: ")
        case "2":
            os.system('cls')   
            logo_senai()
            mostrar_dados(nome, email, tel)
        case '3':
            break
        case _:
            print("Não existe essa função")
            continue