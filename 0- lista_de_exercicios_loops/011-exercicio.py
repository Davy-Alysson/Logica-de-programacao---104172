import os
os.system('cls')

string_original = "Python"

string_reverso = ""

for palavra in string_original:
    string_reverso = palavra + string_reverso

print(f"Original: {string_original}")
print(f"Reverso: {string_reverso}")
