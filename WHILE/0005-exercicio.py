import os
os.system('cls')

soma = 0

for i in range(3):
    while True:
        nota = float(input(f"Digite a {i+1} nota entre 0 e 10: "))
        if nota < 0 or nota > 10:
            print("Nota inválida. \n Tente novamente\n")
            input('Pressione uma tecla para continuar... ')
            os.system("cls")

        else:
            soma += nota
            break

media = soma / 3

if media >= 7:
    print(f"APROVADO com {media:.1f}")
elif 5 < media < 6.9:
    print(f"RECUPERAÇÃO com {media:.1f}")
else:
    print(f"REPROVADO com {media:.1f}")