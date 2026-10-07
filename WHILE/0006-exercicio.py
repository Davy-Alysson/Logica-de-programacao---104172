import os 
import time
os.system('cls')


quantidade_de_notas = 0
soma = 0.0

nota = float(input("Digite sua nota:"))
soma += nota
quantidade_de_notas += 1

while True:
    pergunta = (input("Você deseja adicionar mais uma nota:")).upper()
    if pergunta == 'S':
        quantidade_de_notas += 1
        nota = float(input(f"Digite a {quantidade_de_notas}ª nota:"))
        soma += nota
    elif pergunta == 'N':
        print(f"Média:{soma/quantidade_de_notas:.1f} ")


