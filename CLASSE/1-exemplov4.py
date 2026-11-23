from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #Nome da variável: tipo da variável
    nome: str
    idade: int

lista_clientes = []

for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('Digite seu nome: '),
        idade = int(input("Digite sua idade: "))
    )
    lista_clientes.append(dados_do_cliente)

for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"="*15)