import os
import random
import time
os.system("cls")

saldo = 0.0

print("1 - Depósito")
print("2 - Aposta")
print("3 - Sacar")
print("4 - Extrato")
print("0 - Sair")
while True:
    opcao = input("Escolha uma opção:")


    if opcao == '1':
        deposito = float(input("Quanto você deseja depositar?"))
        saldo += deposito


    elif opcao == '2':
        aposta = float(input("Quanto você quer apostar?"))

        if aposta > saldo:
            print(f"Não é possivel apostar R$ {aposta}, deposite mais dinheiro!")
            continue
        elif aposta <= saldo:
            saldo -= aposta
            print(f"Você apostou R$ {aposta}")

            formas = '🙈', '🙉', '🙊'

            escolha = random.choice(formas)
            escolha1 = random.choice(formas)
            escolha2 = random.choice(formas)

            ganho = escolha == escolha1 == escolha2



        print(time.sleep(1),escolha,time.sleep(1), escolha1,time.sleep(1), escolha2)

        if escolha == escolha1 == escolha2:
            if escolha == '🙈':
                    premio = aposta * 2
            elif escolha == '🙉':
                    premio = aposta * 6
            elif escolha == '🙊':
                    premio = aposta * 10
            saldo += premio
            print(f"PARABÉNS! Você ganhou R$ {premio:.2f}!")
            print(f"Seu saldo atual é: R$ {saldo:.2f}\n")
        else:
            print(f"Você perdeu R$ {aposta:.2f}.")
            print(f"Seu saldo atual é: R$ {saldo:.2f}\n")
    elif opcao == '3':
        saque = float(input("Quanto você deseja sacar?"))
        if saque > saldo:
            print(f"Valor indísponivel em conta")
        else:
            saldo -= saque
            print(f"Você sacou R$ {saque}")

    elif opcao == '4':
         print(f"Você tem R$ {saldo} em conta")

    elif opcao == '0':
         os.system("cls")
         time.sleep(1)
         
         print("FINALIZANDO PROGRAMA")
         time.sleep(1)
         os.system("cls")
         
         print("FINALIZANDO PROGRAMA.")
         time.sleep(1)
         os.system("cls")
         
         print("FINALIZANDO PROGRAMA..")
         time.sleep(1)
         os.system("cls")
         
         print("FINALIZANDO PROGRAMA...")
         time.sleep(2)
         
         os.system('cls')
         
         print("PROGRAMA FINALIZADO")
         
         break
    