# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
quant = float (input('Quanto de Dinheiro Você tem Na Carteira: R$ '))
quant = quant/3.27 
print ('Você Pode Comprar: U${:.2f}'.format(quant))
