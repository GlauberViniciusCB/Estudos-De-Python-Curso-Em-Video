# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também
# um programa que importe esse módulo e use algumas dessas funções.

def aumenta(n):
    n = n + (n*0.10)
    return n
def diminuir(n):
    n = n - (n*0.30)
    return n
def dobro(n):
    return n*2
def metade(n):
    return n/2
