#  Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os 
#  valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar 
#  a digitar valores.
esc_user = ' '
cont =  0
soma = 0
maior = 0
menor = 0
while(esc_user != 'N'):
    num = int(input('Informe Um Número: '))
    esc_user = str(input('Deseja Digitar Mais Números [S/N]: ')).upper() 
    soma = soma + num  
    cont = cont + 1 
    media = soma/cont
    if(cont == 1):
        maior = num
        menor = num 
    else:
        if(num> maior):
            maior = num 
        if(num < menor):
            menor = num 
print('\n')
print('A Média Dos Números Digitado Foi De: {}'.format(media))
print('O Total De Números Digitados Foi De: {}'.format(cont))
print('O Menor Número Digitado Foi: {}'.format(menor))
print('O Maior Número Digitado Foi: {}'.format(maior))
