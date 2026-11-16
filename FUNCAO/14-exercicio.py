import os
os.system('cls')

notas = []

for i in range (3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

def resultado(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'

print(f'A média das notas é: {media:.1f}')
print(f'O aluno está: {resultado(media)}')
