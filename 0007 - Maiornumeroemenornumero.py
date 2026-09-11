import os
os.system("cls")

primeiro_numero = float(input("Digite o primeiro número:"))
segundo_numero = float(input("Digite o segundo número:"))
terceiro_numero = float(input("Digite o terceiro número:")
                        )
os.system("cls")

print("Primeiro número informado:", primeiro_numero)
print("Segundo número informado:", segundo_numero)
print("Terceiro número informado:", terceiro_numero)

maior_numero = max(primeiro_numero, segundo_numero, terceiro_numero)
menor_numero = min(primeiro_numero, segundo_numero, terceiro_numero)

print("O maior número é:", maior_numero)
print("O menor número é:", menor_numero)


