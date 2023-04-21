# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa
# tem que realizar três contagens através da função criada:                           
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2   
# c) uma contagem personalizada

def contador ():
    print('Contagem De 1 Até 10, De 1 Em 1: ', end=' ')
    for i in range (1,11):
        print(i,end=' ')
    print('\nContagem De 10 Até 0, De 2 Em 2:', end=' ')
    for i in range (10,-1,-2):
        print(i,end= ' ')
    print('\n')
    inic = int(input('Digite O Inicio: ')) 
    fim =  int(input('Digite O Fim: '))
    pulo = int(input('Digite O Pulo: '))
    if (pulo == 0):
        pulo = 1
    while(inic > fim and pulo > 0):
        print('Por Favor, Digite Um Fim Maior Que O Início, Caso Queira Uma Contagem Regressiva Digite Um Número Menor Que "0" No Pulo.')
        inic = int(input('Digite O Inicio: ')) 
        fim =  int(input('Digite O Fim: '))
        pulo = int(input('Digite O Pulo: '))
    print(f'Você Solicitou A Contagem Iniciando Em {inic} Terminando Em {fim} Com Saltos De {pulo} Entre Os Números: ',end =' ')
    for i in range(inic,fim,pulo):
        print(f'{i}',end= ' ')

contador()