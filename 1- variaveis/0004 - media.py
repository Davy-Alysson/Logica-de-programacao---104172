import os

os.system("cls")

print("-> SOLICITANDO DADOS <-")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeira_nota = float(input("Digite a primeira nota:"))
segunda_nota = float(input("Digitre a segunda nota:"))

soma = primeira_nota + segunda_nota
subtracao = primeira_nota - segunda_nota
multiplicacao = primeira_nota * segunda_nota
divisao = primeira_nota / segunda_nota
media = soma / 2





print('\n= EXIBINDO DADOS')

print("Nome:", nome)
print("idade:", idade)
print("Primeira nota:", primeira_nota)
print("Segunda nota:", segunda_nota)

print('\n -> EXIBINDO OPERAÇÕES <-')

print("Soma=", soma)
print("Subtração=", subtracao)
print("Multiplicação=", multiplicacao)
print("Divisão=", divisao)
print("Média=", media)
