import os

os.system("cls")

primeira_nota = float(input("Digite sua primeira nota:"))
segunda_nota = float(input("Digite sua segunda nota:"))

media = (primeira_nota + segunda_nota) / 2

if media >= 9:
    print("Você foi aprovado no conceito A,", "e sua nota foi:", media)
elif 9 > media >= 7.5:
    print("Você foi aprovado no conceito B,", "e sua nota foi:", media)
elif 7.5 > media >= 6:
    print("Você foi aprovado no conceito C,", "e sua nota foi:", media)
elif 6 > media >= 4:
    print("Você foi reprovado no conceito D,", "e sua nota foi:", media)
else:
    print("Você foi reprovado no conceito E,", "e sua nota foi:", media)