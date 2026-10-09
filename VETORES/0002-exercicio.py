import os
os.system('cls')

notas = []

for i in range(3):
    nota = float(input(f'Digite a {i + 1}ª:'))
    notas.append(nota)

    media = sum(notas) / len(notas)

print(f'Media = {media:.1f}')

    