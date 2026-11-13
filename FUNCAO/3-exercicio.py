import os
os.system('cls')

def logo_senai():
    print('='*15)
    print(' SENAI - BAHIA')
    print('='*15)

def mostrar_dados(nome, idade):
    print(f'Nome: {nome}\nIdade: {idade}')


logo_senai()
nome = input('Digite seu nome: ')

logo_senai()
idade = int(input("Digite sua idade: "))

mostrar_dados(nome, idade)