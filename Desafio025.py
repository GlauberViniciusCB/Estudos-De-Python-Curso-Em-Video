#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Informe Seu Nome Completo:')).strip()
print('Seu Nome Tem Silva: {} '.format('silva' in nome.lower()))   
