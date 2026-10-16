import os
os.system('cls')

numeros_positivos = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero <= 0:
        numeros_positivos.append(0)
    else:
        numeros_positivos.append(numero)

print(f"Números: {numeros_positivos}")