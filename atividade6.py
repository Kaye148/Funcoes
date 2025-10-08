import os
os.system("cls")

def inflacao(produto):
    if produto < 100:
        produto * 1.10
        return
    else:
        produto * 2.10
        return

produto = float(input("infrome o valor do produto!: "))
 
inflacao = (produto)
 
print(f"{inflacao}")



