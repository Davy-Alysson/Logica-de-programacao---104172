import os
os.system('cls')


def preco_produto():
    preco = float(input('Digite o preço do produto: '))
    if preco < 100:
        preco = preco + (preco * 0.10)
    elif preco >= 100:
        preco = preco + (preco * 0.20)
    return preco

print(f'O preço final do produto é: R${preco_produto():.2f}')




