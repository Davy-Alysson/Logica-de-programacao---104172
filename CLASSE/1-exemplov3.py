from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #Nome da variável: tipo da variável
    nome: str
    idade: int

lista_clientes = []

lista_clientes.append(Cliente('Marta', +.30))
lista_clientes.append(Cliente('José', 40))

for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print('='*15)