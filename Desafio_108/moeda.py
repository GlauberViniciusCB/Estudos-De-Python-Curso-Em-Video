# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também
# um programa que importe esse módulo e use algumas dessas funções.

def aumenta(n = 0):
    n = n + (n*0.10)
    return n
def diminuir(n = 0):
    n = n - (n*0.30)
    return n
def dobro(n = 0):
    return n*2
def metade(n = 0):
    return n/2
def moeda(n ,tipo ='R$'):
   return f'{tipo}{n:.2f}'. replace('.',',')
   