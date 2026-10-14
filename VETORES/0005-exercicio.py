import os 
os.system("cls")

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i + 1}ª nota:"))
    notas.append(nota)

for posicao, nota in enumerate(notas, start=1):
    print(f"{posicao}ª nota: {nota}")

media = sum(notas) / len(notas)

if media >= 7:
    print("APROVADO")
elif media <= 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")

maior_nota = max(notas)
menor_nota = min(notas)

print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")