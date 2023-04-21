# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por 
# Km para viagens de até 200Km e R$0,45 para viagens mais longas.
dis = float(input('Qual A Distãncia Percorrida Em Km ? '))
if(dis <= 200 ):
    total = dis*0.50
    print('O Valor A Ser Pago Pela Distância De {} Km Percorridos, É De: R${:.2f}'.format(dis,total))
else:
    total = dis*0.45
    print('O Valor A Ser Pago Pela Distância De {} Km Percorridos, É De: R${:.2f}'.format(dis,total))

