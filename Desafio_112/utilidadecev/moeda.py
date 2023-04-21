# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também
# um programa que importe esse módulo e use algumas dessas funções.

def aumenta(n = 0,forma = False):
    n = n + (n*0.10)
    return n if forma == False else moeda(n) 
def diminuir(n = 0,forma = False):
    n = n - (n*0.30)
    return n if forma == False else moeda(n) 
def dobro(n = 0, forma = False):
    return n*2 if forma == False else moeda(n)
def metade(n = 0,forma = False):
    return n/2 if forma == False else moeda(n) 
def moeda(n ,tipo ='R$'):
   return f'{tipo}{n:.2f}'. replace('.',',')
def resumo(n):
    print()
    print(f'Preço Analisado: {moeda(n)}')
    print(f'Dobro Do Preço: {moeda(dobro(n))}')
    print(f'Metade Do Preço: {moeda(metade(n))}')
    print(f'Aumento De 10%: {moeda(aumenta(n))}')
    print(f'Redução De 30%: {moeda(diminuir(n))} ')
    return n