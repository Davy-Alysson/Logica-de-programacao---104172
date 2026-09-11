import os
os.system("cls")

macas = int(input("Digite a quantidade de maçãs desejadas:"))

if macas <= 11:
    print(f"O valor total é ", macas * 1.30, 'reais')
elif macas >= 12:
    print(f"O valor total é", macas * 1.00, 'reais')