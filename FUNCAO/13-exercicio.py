import os
import time
os.system('cls')

def ano_nascimento():
    ano = int(input('Digite o ano de nascimento: '))
    idade = time.localtime().tm_year - ano
    return idade

print(f'A idade da pessoa é: {ano_nascimento()} anos')