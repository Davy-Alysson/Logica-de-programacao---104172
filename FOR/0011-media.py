import os
os.system("cls")

soma = 0
media = 0

for i in range(1,5):
    notai = float(input(f"Digite a {i}º nota:"))
    soma =+ notai
    media = soma / 4

print(f"Media:{media:.1f}")