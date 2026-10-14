import os
os.system("cls")

lista_numeros = []
numero_par = []
numero_impar = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1}º número:"))
    
    if numero % 2 == 0:
        numero_par.append(numero)
    else:
        numero_impar.append(numero)

print(f"Numeros pares: {len(numero_par)}")
print(f"Numeros impares: {len(numero_impar)}")