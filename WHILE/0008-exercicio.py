import os
os.system('cls')

quantidade_de_numeros_geral = 0
quantidade_de_numeros_pares = 0
soma_numeros_pares = 0
soma_geral = 0



while True:
    numero = float(input(f"Digite o {quantidade_de_numeros_geral + 1}º número:"))
    if numero % 2 == 0:
        soma_numeros_pares += numero
        quantidade_de_numeros_pares += 1
        soma_geral += numero
        quantidade_de_numeros_geral += 1
    else:
        soma_geral += numero
        quantidade_de_numeros_geral += 1
    
    if numero == 0:
        quantidade_de_numeros_geral -= 1
        break

media_geral = soma_geral / quantidade_de_numeros_geral
media_numeros_pares = soma_numeros_pares / quantidade_de_numeros_pares

print(f"Quantidade de números pares e impares:{quantidade_de_numeros_geral}")
print(f"Média dos pares: {soma_numeros_pares / quantidade_de_numeros_pares}")
print(f"Média geral: {soma_geral / quantidade_de_numeros_geral}")
