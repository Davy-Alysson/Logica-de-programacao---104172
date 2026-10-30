import os
import time
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
            print('GUARDE UMA SÉRIE')
            nome = input("Digite o nome da série: ").strip().upper()
            if nome == '':
                print("Espaço não pode ficar em branco")
            else:
                if nome == nome in lista:
                    print("Série já está guardada")
                else:
                    lista.append(nome)
                    os.system("cls")
                    print("Série guardada com sucesso")
                    time.sleep(1)
                    os.system('cls')
        case 2:
            os.system("cls")
            print("LISTAR SÉRIES")
            if len(lista) == 0:
                print("Sem série guardada")
            else:
                for i, serie in enumerate(lista):
                    print(f"{i + 1}. {serie}")
                print(f'Total de séries: {len(lista)}')
        case 0:
            print("FINALIZANDO DO PROGRAMA")
            input("PRESSIONE PARA FINALIZAR")
            break
        case _:
            print('Opção inválida!')
            input('Pressione uma tecla para continuar...')
            continue