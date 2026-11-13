import os
os.system("cls")

def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

soma = calcular_notas(nota1, nota2)

print(f"Soma = {soma}")
