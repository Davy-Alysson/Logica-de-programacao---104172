import os
import time
os.system('cls')

lista = []

while True:

    print("===MERCADINHO DENDEZEIROS")
    print("1 - Cadastrar produtos")
    print("2 - Listar produtos")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("CADASTRE UM PRODUTO")
            nome = input("Digite o nome do produto: ").strip().upper()
            if nome == '':
                print("Não pode ficar vazio")
            else:
                if nome == nome in lista:
                    print("Esse produto já está em estoque")
                else:
                    lista.append(nome)
                    os.system('cls')
                    print("Produto cadastrado com sucesso!")
                    time.sleep(1)
                    os.system('cls')
        case 2:
            os.system('cls')
            print("PRODUTOS EM ESTOQUE")
            if len(lista) == 0:
                print('Estoque vazio')
            else:
                for i, produto in enumerate(lista):
                    print(f"{i+1}. {produto}")
                print(f"Total de produtos: {len(lista)}")
            
        case 0:
            print("Fim do programa.")
            input("Pressione uma tecla para continuar...")
            break
        case _:
            print("Opção inválida!")
            input("Pressione uma tecla para continuar...")