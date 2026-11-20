import os
import sys
import time
os.system('cls')

depositos = []
saques = []
senha_certa = '123'
saldo = 500.0

def autenticar(senha_certa):
    for i in range(3):
        senha = input('Digite a senha do banco: ')
        if senha == senha_certa:
            print('ACESSO LIBERADO!')
            return True
        else:
            print(f'ACESSO NEGADO você tem {2 - i} tentativas')
            continue
    print('\nNúmero máximo de tentativas atingidas. O sistema será bloqueado por segurança.')
    sys.exit()                

def menu():
    print("=== BANCO COFRINHO = CAIXA ===")
    print('1 - Ver saldo')
    print('2 - Depositar')
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("0 - Sair")
        
def ver_saldo(saldo):
        print(f'Saldo: {saldo: .2f}')
        time.sleep(2)
        os.system('cls')
        
    

def deposito(saldo):
    while True:
        print('=== DEPÓSITO ===')
        depositar = float(input("Quanto deseja depositar? R$ "))
        if depositar <= 0 :
            print('Deposite um valor maior que R$ 0.00')
            escolha_d = input("Deseja voltar para o menu? S ou N: ").strip().upper()
            if escolha_d == "N":
                continue
            elif escolha_d == 'S':
                os.system('cls')
                return saldo
        else:
            print(f"$$$ R${depositar} foi depositado com sucesso! $$$")
            time.sleep(1)
            os.system('cls')
            saldo += depositar
            depositos.append(depositar)
            return saldo
            
def saque(saldo):
    while True:
        print('=== SAQUE ===')
        sacar = float(input('Quanto deseja sacar? R$ '))
        if sacar > saldo:
            print('Saldo insuficiente')
            escolha_s = input("Deseja voltar para o menu? S ou N: ").strip().upper()
            if escolha_s == "N":
                continue
            elif escolha_s == 'S':
                os.system('cls')
                return saldo
        elif sacar > 1000:
            print(f"Limite estourado (R$ {sacar})")
            escolha_s = input("Deseja voltar para o menu? S ou N: ").strip().upper()
            if escolha_s == "N":
                continue
            elif escolha_s == 'S':
                os.system('cls')
                return saldo      
        elif sacar <= 0:
            print("Saque um valor maior que R$ 0.00")
            escolha_s = input("Deseja voltar para o menu? S ou N: ").strip().upper()
            if escolha_s == "N":
                continue
            elif escolha_s == 'S':
                os.system('cls')
                return saldo
        else:
            print(f"$$$ R${sacar} foi sacado com sucesso! $$$")
            saldo -= sacar
            saques.append(sacar)
            return saldo
            
def mostrar_extrato(saldo):
    print("---> EXTRATO <---")
    print(f'\n --- DEPÓSITOS ({len(depositos)})---')
    if not depositos:
        print(f'Nenhum depósito realizado.')
    else:
        for valor in depositos:
            print(f'(+) R$ {valor:.2f}')
    print(f'\n  --- SAQUES ({len(saques)})---')
    if not saques:
        print("Nenhum saque realizado.")
    else:
        for valor in saques:
            print(f"(-) R$ {valor:.2f}")

    print(f'\n Saldo atual = R$ {saldo:.2f}')

while True:
    autenticar(senha_certa)
    menu()
    escolha = input('Escolha: ')

    match escolha:
        case '1':
            ver_saldo(saldo)
            
        case '2':
            saldo = deposito(saldo)
            
        case '3':
            saldo = saque(saldo)
            
        case '4':
            mostrar_extrato(saldo)
            
        case '0':
            time.sleep(0.7)
            print('Encerrando banco.')
            time.sleep(0.7)
            print('Encerrando banco..')
            time.sleep(0.7)
            print('Encerrando banco...')
            time.sleep(0.7)
            break
        case _:
            print('Opção invalida')          