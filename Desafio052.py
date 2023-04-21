#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont=0
print('\n')
num = int(input('Digite Um Número Inteiro: '))
for i in range(1,num+1):
    primo = num%i
    if(primo == 0):
        cont=cont+1
if(cont == 2):
    print('\n\033[32mO Número {} É Um Número Primo!\033[m'.format(num))
elif(cont!=2):
    print('\n\033[31mO Número {} Não É Primo!\033[m'.format(num))