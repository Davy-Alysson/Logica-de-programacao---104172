import os
os.system('cls')

total_de_familias = 0
media_salario_populacao = 0.0
media_salario_filhos = 0.0
quantidade_de_filhos = 0
maior_salario = 0.0
menor_salario = 0.0
salario = 0.0
print('1 - Adicionar família')
print('2 - Sair e exibir resultados')

while True:
    escolha = input('Escolha: ')
    if escolha == '1':
        salario_familia = float(input("Qual o salário da sua família:"))
        numero_de_filhos = int(input("Quantos filhos tem na sua família:"))
        total_de_familias += 1
        quantidade_de_filhos += numero_de_filhos
        salario += salario_familia 

    if total_de_familias == 1:
            maior_salario = salario_familia
            menor_salario = salario_familia
    else:
        if menor_salario > maior_salario:
            maior_salario = salario_familia
        if maior_salario < menor_salario:
            menor_salario = salario_familia

    if escolha == '2':
        if total_de_familias == 0:
            print('Nenhum dado encontrado')
            break
        
        else:
            media_populacao = salario / total_de_familias
            media_filhos = quantidade_de_filhos / total_de_familias

        print(f'Total de famílias: {quantidade_de_filhos}')
        print(f'Média do salário da população: {media_populacao}')
        print(f'Média do número de filhos: {media_filhos}')
        print(f'Maior salário: {maior_salario}')
        print(f'Menor salário: {menor_salario}')

        break

