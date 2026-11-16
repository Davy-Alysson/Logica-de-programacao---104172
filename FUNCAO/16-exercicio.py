import os
os.system('cls')

def media_notas(notas):
    return sum(notas) / len(notas)

def mostrar_notas(notas):
    for i, nota in enumerate(notas, start=1):
        print(f'{i}ª Nota: {nota:.1f}')

def status_do_aluno(media):
    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    return resultado
notas = []


for i in range (2):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota: '))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            break
        else:
            print(f"Nota invalida, tente novamente!")

media = media_notas(notas)

mostrar_notas(notas)
print(f"Média: {media}")
print(f"Situação do aluno: {status_do_aluno(media)}")
