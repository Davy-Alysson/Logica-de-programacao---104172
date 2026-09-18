import os
os.system("cls")

altura = float(input("Digite sua altura:"))

print('M para Masculino')
print('F para Feminino')

sexo = input("Digite seu sexo:")

match sexo:
    case "M":
        print(f'Seu peso ideal e: {72.7 * altura - 58:.2f}')
    case "F":
        print(f'Seu peso ideal e: {62.1 * altura- 44.7:.2f}')