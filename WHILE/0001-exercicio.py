import os
os.system("cls")

saldo = 0.0


while True:
    
    print('BANCO MASTER')
    print('1 - Depósito')
    print('2 - Saque')
    print('3 - Pix')
    print('4 - Extrato')
    print('0 - Sair')
    
    
    escolha = input("ESCOLHA:")
    
    
    
    if escolha == '1':
        deposito = float(input("Quanto você quer depositar?"))
        saldo += deposito
        print(f"Você depositou R$ {deposito}")

    if escolha == '2':
        saque = float(input("Quanto você quer sacar?"))
        if saque <= saldo:
            saldo -= saque
            print(f"Você sacou R$ {saque}")
        else:
            print(f'Você não tem R$ {saque} em conta')
    if escolha == '3':
        pessoa = str(input(f'Para quem você quer enviar um pix?')).lower()
        pix = float(input(f"Quanto você quer enviar para {pessoa}?"))
        print(f"S - SIM")
        print(f"N - NÃO")
        confirmacao = str(input(f"Confirme")).upper()
        
        if confirmacao == 'S' and pix <= saldo:
            print(f"{pix} foi enviado com sucesso para {pessoa}")
        elif confirmacao == 'N':
            print(f'Pix não enviado')
        elif pix > saque:
            print(f"Você não tem R$ {pix} em conta")
    if escolha == '4':
        print(f'Você tem R$ {saldo} em conta')
    if escolha =='0':
        print()
        print("PROGRAMA FINALIZADO")

        break

        

        
