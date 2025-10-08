import os 

def limpar_tela():
    os.system("cls")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    return n1 / n2 if n2 != 0 else "divisão por zero."

def multiplicar(n1, n2):
    return n1 * n2 

def mostar_resultado(soma,sub, div, multi):
    print(f"resultado: {soma}")
    print(f"resultado: {sub}")
    print(f"resultado: {div}")
    print(f"resultado: {multi}")



primeiro_numero = int(input("digite um número: "))
segundo_numero = int(input("digite um número"))

soma = somar (primeiro_numero, segundo_numero)
sub = subtrair (primeiro_numero, segundo_numero)
div = dividir (primeiro_numero, segundo_numero)
multi = multiplicar (primeiro_numero, segundo_numero)

mostar_resultado(soma, sub, div, multi)