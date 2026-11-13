import os
os.system('cls')

def numero_positivo(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Neutro'

numero = int(input('Digite um número: '))

resultado = numero_positivo(numero)

print(f'O número: {numero} é {resultado}')