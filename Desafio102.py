# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e
# outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
# do fatorial.
def fatorial (num,show=0):
    fat = 1
    if(show == True):
        for numeros in range(num,0,-1):
            fat = fat * numeros
            if(numeros != 1):
                print(numeros,end = ' X ')
            else:
                print(f'{numeros} =  {fat}')    
        return fat,show
    else:
        for numeros in range(num,0,-1):
            fat = fat * numeros 
        return print(fat)

fatorial(5,True)
fatorial(5)
fatorial(7,True)