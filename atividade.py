import os
os.system("cls")



def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("ímpar")

print("solicitando dados. ")
numero = int(input("digite um número: "))

#chamando a função.
par_ou_impar(numero)