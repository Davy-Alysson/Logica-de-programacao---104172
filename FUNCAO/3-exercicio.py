import os
os.system('cls')

def logo_senai():
    print('='*15)
    print(' SENAI - BAHIA')
    print('='*15)

def mostrar_dados(nome, email, telefone):
    print(f'Nome: {nome}\nEmail: {email}\nTelefone é {telefone}')


logo_senai()
nome = input('Digite seu nome: ')

logo_senai()
email = input('Digite seu email: ')

logo_senai()
telefone = input('Digite seu telefone: ')

mostrar_dados(nome, email, telefone)