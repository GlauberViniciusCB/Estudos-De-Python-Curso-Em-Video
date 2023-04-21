#  Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
# sorteados pela função anterior.
from random import randint
numeros = []
def sorteia():
    i = 0
    while(i < 5):
        num = randint(0,100)
        numeros.append(num)
        i= i + 1
    print(f'Os Números Sorteados Foram: {numeros}')
def somaPar():
    i = 0 
    maior = 0
    while(i<len(numeros)):
        if(i == 0):
            maior = numeros[i]
        else:
            if(numeros[i]> maior):
                maior = numeros[i]  
        i= i + 1
    print(f'O Maior Número Entre Os Digitados Foi: {maior} ')
sorteia()
somaPar()