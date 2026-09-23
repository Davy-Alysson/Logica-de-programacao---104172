import os
os.system("cls")
pares = 0
impares = 0
for i in range(1, 6):
    numero = int(input(f"Digite o {i}º:"))

    if numero % 2 ==0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
