import os 
os.system("cls")

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i + 1}ª nota:"))
    notas.append(nota)

for posicao, nota in enumerate(notas, start=1):
    print(f"{posicao}ª nota: {nota}")

media = sum(notas) / len(notas)

print(f"Média: {media}")