from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:

    nome: str
    telefone: int
    email: str

lista_dados = []

for i in range(2):
    dados_do_cliente = Cliente(
    nome = input('Digite seu nome: '),
    telefone = input('Digite seu telefone: '),
    email = input('Digite seu e-mail: ')
    )
    lista_dados.append(dados_do_cliente)

for cliente in lista_dados:
    print(f'Nome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'E-mail: {cliente.email}')
    print('='*15)
