import os
os.system("cls")

print("1 - Pagamento a vista")
print("2 - Pagamento a prazo")

escolha = input("Digite a forma de pagamento:")
valor = float(input("Digite o valor do produto:"))
valor_do_desconto = (valor * 0.10)
valor_com_desconto = (valor - valor_do_desconto)

match escolha:
    case "1":
        print(f"Valor do produto: R${valor}")
        print("Forma de pagamento : a vista")
        print(f"Valor do desconto R${valor_do_desconto}")
        print(f"Total a pagar: R${valor_com_desconto}")
    case "2":
        parcelas = int(input("Digite a quantidade de parcelas em ate 6 vezes:"))
        if parcelas <= 6:
            print(f"Valor do produto: R${valor}")
            print("Forma de pagamento: a prazo")
            print("Quantidade de parcelas:", parcelas)
            print(f"Valor por parcela: R${valor / parcelas:.2f}")
            print(f"Total a pagar: R${valor}")
        else:
            print("Quantidade de parcelas invalidas")
            

        