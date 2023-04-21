# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome 
# separadamente.
nome = str(input('Digite Um Nome: ')).strip()
nomes = nome.split()
print('Seu Nome Completo É: {}'.format(nome))
print('Seu Primeiro Nome É: {}'. format(nomes[0]))
# Poderia Ter Usado O -1 Que Tambem Mostra O Ultimo Item Da Lista.
nomes.reverse()
print('Seu Ultimo Nome É: {}'.format(nomes[0]))   