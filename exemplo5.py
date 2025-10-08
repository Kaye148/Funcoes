import os
import time

os.system("cls")

def limpa_tela():
    os.system("cls")
    time.sleep(3) #espere 3 segundos.

# função com parâmetros e com retorno.
def somar(n1, n2):
    return n1 + n2

# função com parâmetro e sem retorno.
def mostrar_resultado(soma):
    print(f"resultado: {soma}")

#código principal.


limpa_tela() #chamando a funcao.

primeiro_numero = int(input("digite um número: "))
segundo_numero = int(input("digite um número: "))

soma = somar(primeiro_numero, segundo_numero)

mostrar_resultado(soma) # chamando a função
