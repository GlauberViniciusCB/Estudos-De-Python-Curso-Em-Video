# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float (input('Informe A Largura Da Parede:'))
altura  = float (input('Informe A Altura Da Parede: '))
total = largura*altura
final = total//2
print('Será Necessário {:.0f} Litros, Para Pintar {} M² '.format(final,total))
