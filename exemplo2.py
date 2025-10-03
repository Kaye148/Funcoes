import os 
os.system

def saudacao(nome, idade, altura, peso):
    print(f"Olá,{nome}! Bem-Vindo !")
    print(f"sua idade é {idade} anos")
    print(f"sua altura é de {altura:.2f}")
    print(f"você pesa {peso}")

nome = input("digite seu nome: ")
idade = int(input("digite seu idade: "))
altura = float(input("informe sua altura: "))
peso = float(input("informe seu peso: "))

saudacao(nome, idade, altura, peso)

