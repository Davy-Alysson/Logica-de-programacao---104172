import os
os.system('cls')

def calculo_imc():
    peso = float(input("Quantos kg você pesa? "))
    altura = float(input("Qual sua altura em metros? "))

    imc = peso / (altura ** 2)

    return imc

def classificacao():
    if calculo_imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 < calculo_imc < 24.9:
        return 'Peso normal'
    elif 25 < calculo_imc < 29.9:
        return 'Sobrepeso'
    elif 30 < calculo_imc < 34.9:
        return 'Obesidade grau 1'
    elif 35 < calculo_imc < 39.9:
        return 'Obesidade grau 2'
    else:
        return 'Obesidade grau 3'

def recomendacao():
    if calculo_imc < 18.5:
        return 'Consulte um nutricionista para orientação'
    elif 18.5 < calculo_imc < 24.9:
        return 'Mantenha hábitos saudáveis'
    elif 25 < calculo_imc < 29.9:
        return 'Considere uma dieta balanceada e atividade física'
    elif 30 < calculo_imc < 34.9:
        return 'Procure orientação de um profissional de saúde'
    elif 35 < calculo_imc < 39.9:
        return 'Consulte um médico para avaliação e orientação'
    else:
        return 'Busque assistência médica imediatamente'


calculo_imc()
print(f'Você está {classificacao()}')
print(f'Você deve {recomendacao()}')

