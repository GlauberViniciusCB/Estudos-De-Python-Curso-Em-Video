# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e 
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido 
# informado corretamente.
def ficha (name='Desconhecido',gols=0):
    print(f'Nome: {name}')
    print(f'Quantidade De Gols: {gols}')

nome = str(input('Digite O Nome Do Jogador: '))
quant = str(input('Quantos Gols Marcados? '))
if quant.isnumeric():
    quant= int(quant)
else:
    quant = 0
if(nome.strip() == ''):
    ficha(gols = quant )
else:
    ficha(nome,quant)
