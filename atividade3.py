import os 
os.system("cls")

def tobuada(numero):
    for i in range(1,11):
        print(f"o produto entre {i} x {numero} = {i*numero}")

numero = int(input("informe um número: "))

tobuada(numero)
