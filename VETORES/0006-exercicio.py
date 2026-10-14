import os
os.system("cls")

lista_numeros = []

for i in range(5):
    numero = int(input(f'Digite o {i + 1}º número:'))
    lista_numeros.append(numero)

maior_num = max(lista_numeros)
menor_num = min(lista_numeros)

print(f"Números: {lista_numeros}")


print(f'Maior número: {maior_num}')
print(f'Menor número: {menor_num}')