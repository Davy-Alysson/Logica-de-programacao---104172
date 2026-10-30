import os
os.system('cls')

lista_nome = []

while True:
    print('HOSPITAL BVL')
    print('1 - Cadastrar jogador')
    print('2 - Listar')
    print('3 - Atualizar')
    print('4 - Excluir')
    print('0 - Sair')

    opcao = int(input("Escolha: "))

    match opcao:
        case 1:
            nome = input("Digite o nome: ").strip()
            sobrenome = input("Digite o sobrenome: ").strip()
            posicao = input('Digite a posicao do jogador: ').strip()
            numero = input('Digite a numeração: ')
            nome_e_sobrenome = nome + ' ' + sobrenome
            juncao = nome_e_sobrenome + '|' + posicao + '|' + numero
            if nome_e_sobrenome == '':
                print("Não pode deixar em branco")
            else:
                if nome_e_sobrenome == nome_e_sobrenome in lista_nome:
                    print("Pessoa já cadastrada. ")
                else:
                    lista_nome.append(juncao)
                    print(f"{juncao} cadastrado(a) com sucesso!")
        case 2:
            print('LISTAR JOGADORES')

            if len(lista_nome) == 0:
                print("Sem jogador cadastrado")
            else:
                for i, jogador in enumerate(lista_nome):
                    print(f'{i+1}. {jogador}')
                print(f'Total de jogadores: {len(lista_nome)}')
        case 3:
            print('ATUALIZAÇÃO JOGADORES')

            if len(lista_nome) == 0:
                print("Sem jogador cadastrado.")
            else:
                # Exibe a lista para o utilizador escolher o número
                for i, jogador in enumerate(lista_nome, start=1):
                    print(f"{i}. {jogador}")

                numero = input("\nDigite o número do jogador que deseja atualizar: ").strip()

                if numero.isdigit():
                    indice = int(numero) - 1

                    if 0 <= indice < len(lista_nome):
                        print(f"Jogador selecionado: {lista_nome[indice]}")
                        novo_nome = input("Digite o novo nome: ").strip()
                        novo_sobrenome = input("Digite o novo sobrenome: ").strip()
                        nova_posicao = input("Digite a nova posição: ").strip()
                        nova_numeracao = int(input("Digite o novo numero do jogador: "))

                        if not novo_nome or not novo_sobrenome or not nova_posicao or not nova_numeracao:
                            print("Erro: O nome, sobrenome, posição ou numeração não podem ficar em branco!")
                        else:
                            lista_nome[indice] = f"{novo_nome} {novo_sobrenome} {nova_posicao} {nova_numeracao}"
                            print("Jogador atualizado com sucesso!")
                    else:
                        print("Número de jogadores inexistente!")
                else:
                    print("Por favor, digite um número válido!")
        case 4:
            print("\n--- EXCLUIR JOGADOR ---")
            if len(lista_nome) == 0:
                print("Sem jogador cadastrado.")
            else:
                for i, jogador in enumerate(lista_nome, start=1):
                    print(f"{i}. {jogador}")

                numero = input("\nDigite o número do jogador que deseja remover: ").strip()

                if numero.isdigit():
                    indice = int(numero) - 1

                    if 0 <= indice < len(lista_nome):
                        removido = lista_nome.pop(indice)
                        print(f"jogador '{removido}' removido com sucesso!")
                    else:
                        print("Número de jogador inexistente!")
                else:
                    print("Por favor, digite um número válido!")
        case 0:
            print('Encerrando o sistema...')
            break

        case _:
            print('Opção inválida! Tente novamente.')
            input("Pressione qualquer botão para continuar... ")