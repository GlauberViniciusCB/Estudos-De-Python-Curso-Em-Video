# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Informe Um Ano Para Análise: '))
if(ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0):
    print('O Ano {} É Bissexto!'.format(ano))
else: 
    print('O Ano {} Não É Bissexto!'.format(ano))