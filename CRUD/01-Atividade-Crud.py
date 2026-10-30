import os
os.system('cls')

lista_nome = []

while True:
    print('HOSPITAL BVL')
    print('1 - Cadastrar paciente')
    print('2 - Listar')
    print('3 - Atualizar')
    print('4 - Excluir')
    print('0 - Sair')

    opcao = int(input("Escolha: "))

    match opcao:
        case 1:
            nome = input("Digite o nome: ").strip()
            sobrenome = input("Digite o sobrenome: ").strip()
            nome_e_sobrenome = nome + ' ' + sobrenome
            if nome_e_sobrenome == '':
                print("Não pode deixar em branco")
            else:
                if nome_e_sobrenome == nome_e_sobrenome in lista_nome:
                    print("Pessoa já cadastrada. ")
                else:
                    lista_nome.append(nome_e_sobrenome)
                    print(f"{nome_e_sobrenome} cadastrado(a) com sucesso!")
        case 2:
            print('LISTAR PACIENTES')

            if len(lista_nome) == 0:
                print("Sem paciente cadastrado")
            else:
                for i, paciente in enumerate(lista_nome):
                    print(f'{i+1}. {paciente}')
                print(f'Total de pacientes: {len(lista_nome)}')
        case 3:
            print('ATUALIZAÇÃO PACIENTES')

            if len(lista_nome) == 0:
                print("Sem paciente cadastrado.")
            else:
                # Exibe a lista para o utilizador escolher o número
                for i, paciente in enumerate(lista_nome, start=1):
                    print(f"{i}. {paciente}")

                numero = input("\nDigite o número do paciente que deseja atualizar: ").strip()

                if numero.isdigit():
                    indice = int(numero) - 1

                    if 0 <= indice < len(lista_nome):
                        print(f"Paciente selecionado: {lista_nome[indice]}")
                        novo_nome = input("Digite o novo nome: ").strip()
                        novo_sobrenome = input("Digite o novo sobrenome: ").strip()

                        if not novo_nome or not novo_sobrenome:
                            print("Erro: O nome e o sobrenome não podem ficar em branco!")
                        else:
                            lista_nome[indice] = f"{novo_nome} {novo_sobrenome}"
                            print("Paciente atualizado com sucesso!")
                    else:
                        print("Número de paciente inexistente!")
                else:
                    print("Por favor, digite um número válido!")
        case 4:
            print("\n--- EXCLUIR PACIENTE ---")
            if len(lista_nome) == 0:
                print("Sem paciente cadastrado.")
            else:
                for i, paciente in enumerate(lista_nome, start=1):
                    print(f"{i}. {paciente}")

                numero = input("\nDigite o número do paciente que deseja remover: ").strip()

                if numero.isdigit():
                    indice = int(numero) - 1

                    if 0 <= indice < len(lista_nome):
                        removido = lista_nome.pop(indice)
                        print(f"Paciente '{removido}' removido com sucesso!")
                    else:
                        print("Número de paciente inexistente!")
                else:
                    print("Por favor, digite um número válido!")
        case 0:
            print('Encerrando o sistema...')
            break

        case _:
            print('Opção inválida! Tente novamente.')
            input("Pressione qualquer botão para continuar... ")