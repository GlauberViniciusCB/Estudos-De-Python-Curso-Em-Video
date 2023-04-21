# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float (input('Informe O Valor Do Produto: R$'))
desconto = valor*0.05
final = valor - desconto
print('O Valor Do Seu Produto Com O Desconto De 5% Será De: {:.2f}'.format(final))