import os
os.system("cls")

soma = 0

print(f"Valor inicial da Variavel: {soma}")

for i in range(3):
    numero = int(input("Digite um numero para somar:"))
    soma = soma + numero
    print(f'Valor temporario da variavel soma: {soma}')

print(f"Valor final da variavel soma: {soma}")