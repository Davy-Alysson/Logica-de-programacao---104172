import os
import time
os.system("cls")

numeroi = int(input("Digite um número inicial:"))
numerof = int(input("Numero final:"))
if numeroi < numerof:
    for i in range(numeroi,numerof + 1,1):
        print(i)
        time.sleep(1)
elif numeroi > numerof:
    for i in range(numeroi,numerof + 1,-1):
        print(i)
        time.sleep(1)

     

