import os 
os.system("cls")

for i in range (3):
    nota = float(input("digite uma nota: "))

def media(nota):
    return (nota + nota + nota) / 3

resultado_media =media(nota)

print(f"sua média foi de {resultado_media:.1f}")
