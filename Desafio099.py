# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa 
# tem que analisar todos os valores e dizer qual deles é o maior.

 
def maior(*num):
    i = 0
    maior_ = 0
    while (i < len(num)):
        print(num[i],end= ' ')
        if(i == 0):
            maior_ = num[i]
        else:
            if(num[i] > maior_):
                maior_ = num[i] 
        i = i + 1  
    print(f'\nForam Informados {len(num)} O Maior Número Entre  Os Digitados Foi: {maior_}')



maior(2,3,1,-2)
maior(4,2,1,7,-1,-2)
maior(4)
maior(-12,-4,-6,-1,-4)