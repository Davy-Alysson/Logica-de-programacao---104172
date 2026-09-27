import os
os.system('cls')

sentenca = "Os loops sao felizes"
vogais = ('aeiou')
quantidade_de_vogais = 0
quantidade_de_consoantes = 0

for palavra in sentenca.lower():
    if palavra.isalpha():
        if palavra in vogais:
            quantidade_de_vogais += 1
        else:
            quantidade_de_consoantes += 1

print(f"Vogais: {quantidade_de_vogais}")
print(f"Consoantes: {quantidade_de_consoantes}")


