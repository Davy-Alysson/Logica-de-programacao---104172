from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Pacientes:
    nome: str
    idade: int
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print('='*15)
        print(f'Nome = {self.nome}')
        print(f'idade = {self.idade}')
        print(f'Telefone = {self.telefone}')
        print(f'Endereço = {self.endereco}')
    
    def dados_n_d(self):
        print('='*15)
        print(f'Nome = {self.nome}')
        print(f'idade = {self.idade}')

    def dados_n_tel(self):
        print('='*15)
        print(f'Nome = {self.nome}')
        print(f'Telefone = {self.telefone}')
        
lista_pacientes = []

dados_do_paciente = Pacientes(
    nome = input('Digite seu nome: '),
    idade = input('Digite sua idade: '),
    telefone = input('Digite seu telefone: '),
    endereco = input('Digite seu endereço: ')

)
lista_pacientes.append(dados_do_paciente)


for paciente in lista_pacientes:
    paciente.mostrar_dados()
for paciente in lista_pacientes:
    paciente.dados_n_d()
for paciente in lista_pacientes:
    paciente.dados_n_tel()