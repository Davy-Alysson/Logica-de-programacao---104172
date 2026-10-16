import os
os.system('cls')

pratos = []
precos = []

while True:
    print("Código     Prato          Valor")
    print("  1       Picanha         25,00")
    print("  2       Lasanha         20,00")
    print("  3       Strogonoff      18,00")
    print("  4       Bife Acebolado  15,00")
    print("  5       Pão com ovo     5,00")
    
    escolha = input("\n Escolha uma opção: ")
    
    if escolha == '1':
        prato = 'Picanha'
        preco = 25 
    elif escolha == '2':
        prato = 'Lasanha'
        preco = 20
    elif escolha == '3':
        prato = 'Strogonoff'
        preco = 18
    elif escolha == '4':
        prato = 'Bife Acebolado'
        preco = 15
    elif escolha == '5':
        prato = 'Pão com ovo'
        preco = 5
    else:
        print("Opção invalida")
        
    if escolha >= '1' and escolha <= '5':
        pratos.append(prato)
        precos.append(preco)
        
    continuar = input('Deseja escolher outro prato? \nResponda com S ou N').upper()
    if continuar == 'N':
        break
    os.system('cls')
    
if sum(precos) == 0:
    print('\nNenhum prato selecionado')
else:
    print('\n PRATOS ESCOLHIDOS')
    for i in enumerate(pratos, start=1):
        print(f'{i}º prato: {prato}')
    
    print(f'\n Total: R$ {sum(precos)}')

print('\n Volte sempre!')