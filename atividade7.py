import os
os.system("cls")

def ano_nascimento():
    anos_nasc = int(input("informe o ano que você nasceu: "))
    return 2025 - anos_nasc

resposta_nascimento = ano_nascimento()

print(f"a sua idade é: {resposta_nascimento} anos.")