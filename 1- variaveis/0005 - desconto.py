import os

os.system("cls")

print("SOLICITANDO DADOS")
valor = float(input("Digite o valor: "))
print("\n-> %")
porcentagem_de_desconto = float(input("Digite a porcentagem: "))


desconto = valor * (porcentagem_de_desconto / 100)
valor_com_desconto = valor - desconto

print("\n -> EXIBINDO DESCONTO")
print('Valor com desconto :', valor_com_desconto)