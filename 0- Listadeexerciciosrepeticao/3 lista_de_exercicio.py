import os
os.system("cls")

while True:
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
    salario = float(input("Digite seu salario:"))
    print("F -> Feminino" \
    "      M -> Masculino")
    sexo = input("Digite seu sexo:").upper()
    print(" S -> Solteiro(a)" \
    " C -> Casado(a)" \
    " V -> Viuvo(a)" \
    " D -> Divorciado(a))")
    estado_civil = input('Digite seu estado civil:').upper()

    if len(nome) > 3 and 0 <= idade <= 150 and salario > 0 and sexo in ['F', 'M'] and estado_civil in ['S', 'C', 'V', 'D']:
        print("VALIDO")
        print(f"Seu nome e {nome}")
        print(f"Sua idade e {idade}")
        print(f"Seu salario e {salario}")
        print(f"Seu sexo e {sexo}")
        print(f"Seu estado civil e {estado_civil}")
        break
    else:
        print("Alguma informacao e invalida")
        print("Tente novamente")

        
        