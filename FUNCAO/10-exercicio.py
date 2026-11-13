import os
os.system('cls')

def soma_numeros(num1, num2):
    resultado = num1 + num2
    return resultado
def subtracao_numeros(num1, num2):
    resultado = num1 - num2
    return resultado
def multiplicacao_numeros(num1, num2):
    resultado = num1 * num2
    return resultado
def divisao_numeros(num1, num2): 
    if num2 != 0:
        resultado = num1 / num2
        return resultado
    else:
        return "Erro: Divisão por zero não é permitida."

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print(f"O resultado da soma é: {soma_numeros(numero1, numero2)}")
print(f"O resultado da subtração é: {subtracao_numeros(numero1, numero2)}")
print(f"O resultado da multiplicação é: {multiplicacao_numeros(numero1, numero2)}")
print(f"O resultado da divisão é: {divisao_numeros(numero1, numero2):.2f}")
