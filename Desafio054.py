# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
#  maioridade e quantas já são maiores.
from datetime import date
cont_Maior = 0
cont_Menor = 0 
for i in range(1,8):
    data= int(input('Informe O Ano De  Nascimento Da {}° Pessoa: '.format(i)))
    atual = date.today().year - data 
    if(atual < 18):
        cont_Menor = cont_Menor + 1
    else:
        cont_Maior = cont_Maior + 1
print('O Total De Pessoas Que Ainda Não Atingiram A Maior Idade: {}'.format(cont_Menor))
print('O Total De Pessoas Que Atingiram A Maior Idade: {}'.format(cont_Maior))
