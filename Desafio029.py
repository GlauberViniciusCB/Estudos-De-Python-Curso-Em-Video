#  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele 
#  foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual A Velocidade Do Carro ? '))
if( vel > 80):
    multa= vel-80
    multa= multa*7.00
    print('Você Ultrapassou A Velocidade Máxima. A Multa Será No Valor De: R$ {:.2f}'.format(multa))
else:
    print('Sua Velocidade É De {} Km/h, Você Não Será Multado.'.format(vel))

