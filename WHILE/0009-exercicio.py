import os
import time
os.system('cls')

salario_total = 0
quantidade_de_pessoas = 0
quantidade_de_mulheres_com_salario = 0
menor_idade = 0
maior_idade = 0

print("1 - ADICIONAR PESSOA")
print("2 - EXIBIR RESULTADOS")
print("3 - SAIR")

while True:
    escolha = input("ESCOLHA UMA OPÇÃO:")
    if escolha == '1':
        idade = int(input("Informe sua idade:"))
        print("F - FEMININO")
        print("M - MASCULINO")
        genero = input("Informe seu gênero:").upper()
        salario = float(input("Informe seu salário:"))
        quantidade_de_pessoas += 1
        salario_total += salario
        continue
        
    if genero == 'F' and salario >= 5000:
        quantidade_de_mulheres_com_salario += 1
        
    if quantidade_de_pessoas == 1:
        maior_idade = idade
        menor_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade
    
    if escolha == '2':
        print(f"A média salarial é: {salario_total / quantidade_de_pessoas}")
        print(f"A maior idade é:{maior_idade}")
        print(f"A menor idade é:{menor_idade}")
        print(f"A quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_de_mulheres_com_salario}")
    if escolha == '3':
        os.system('cls')
        print("FINALIZANDO PROGRAMA")
        time.sleep(1)
        os.system('cls')
        print("FINALIZANDO PROGRAMA.")
        time.sleep(1)
        os.system('cls')
        print("FINALIZANDO PROGRAMA..")
        time.sleep(1)
        os.system('cls')
        print("FINALIZANDO PROGRAMA...")

        time.sleep(1)
        os.system('cls')
        print("PROGRAMA FINALIZADO.")

        break
        
        