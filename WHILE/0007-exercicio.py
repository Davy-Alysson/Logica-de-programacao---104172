import os 
import time
os.system('cls')


quantidade_de_notas = 0
soma = 0.0



while True:
    nota = float(input(f"Digite a {quantidade_de_notas + 1}ª:"))
    if nota > 0:
        quantidade_de_notas += 1
        soma += nota
    elif nota < 0:
        print(f"Média: {soma / quantidade_de_notas}")
        break



