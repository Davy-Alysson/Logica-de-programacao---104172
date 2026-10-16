import os
os.system('cls')

vetor_notas = []

for i in range(3):
    nota = float(input(f'Digite a {i + 1}ª nota:'))
    vetor_notas.append(nota)

for i in range(3):
    print(f'Nota: {vetor_notas[i]}')