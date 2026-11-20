import os
os.system('cls')

def autenticar():
    matricula = input('Digite sua matricula: ')
    senha = int(input("Digite sua senha: "))

    print("Autenticado com sucesso!")
    return matricula, senha

def entradas():
    salario_base = float(input("Digite o salário base: R$ "))
    salario_base += salario_b
    while True:
        vale_transporte = input("Possui vale transporte? S / N : ").strip().upper()
        match vale_transporte:
            case 'S':
                valor_vt = float(input('Qual o valor do vale transporte? R$ '))
                valor_vt += valor_do_vt
                break
            case 'N':
                print("Não possui vale transporte.")
                break
            case _:
                print("Não existe essa opção.")
                continue


    vale_refeicao = float(input("Qual o valor do vale refeição? R$ "))
    vale_refeicao += valor_do_vr
    while True:
        dependentes = int(input("Quantos dependentes? "))
        if dependentes < 0:
            print("Número inválido")
            continue
        else:
            dependentes += n_dependentes
            break
    return salario_base, vale_transporte, vale_refeicao, dependentes
    

    
            
    


#Valores
salario_b = 0
valor_do_vt = 0
valor_do_vr = 0
n_dependentes = 0








autenticar()
entradas()
print(f"{salario_b}")
print(f"{valor_do_vt}")
print(f"{valor_do_vr}")
print(f"{n_dependentes}")
