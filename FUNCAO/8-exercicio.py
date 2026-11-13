import os
os.system('cls')

def numero_impar_ou_par(numero):
    if numero % 2 != 0:
        return 'O número é ímpar'
    else:
        return 'O número é par'

numero = int(input('Digite um número: '))

resultado = numero_impar_ou_par(numero)

print(resultado)