# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 
# 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles 
# (desconsiderando o flag).
num = 0
soma = 0
cont = 0
while(num != 999):
    num = int(input('Informe Um Número, Caso Deseje Finalizar Digite \033[33m999\033[m: ')) 
    if(num != 999):
        soma = soma + num
        cont= cont + 1
print('\nForam Digitados {} Números, E A Soma Final Resulta Em: {} '.format(cont,soma))        


