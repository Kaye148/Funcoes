import os
os.system ("cls")

for i in range (2):
    nota = float(input("informe sua nota: "))

def media(nota):
    return nota * 2 / 2

def ap_rp(media):
    if media > 7:
        print("aprovado")
    else: media < 7
    print("reprovado")

resultado = ap_rp(media)

print(f"{resultado}")