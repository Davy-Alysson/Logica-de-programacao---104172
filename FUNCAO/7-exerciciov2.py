import os
os.system("cls")

def calcular_notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def verificar_nota(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_notas(nota1, nota2)
situacao = verificar_nota(media)

print(f"Media = {media}")
print(f"Resultado = {situacao}")
