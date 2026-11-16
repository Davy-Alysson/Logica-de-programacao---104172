import os
os.system('cls')

def media_notas():
    return sum(notas) / len(notas)

def mostrar_notas(media, notas):
    for i, nota in enumerate(notas, start=1):
        print(f'{i}ª Nota: {nota:.1f}')
    print(f'Média: {media:.1f}')

notas = []

for i in range (3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)

os.system('cls')

media = media_notas()

mostrar_notas(media, notas)