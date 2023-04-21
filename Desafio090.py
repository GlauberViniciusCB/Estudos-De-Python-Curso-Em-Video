# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um 
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
cont = 0
jogadores = {'Jogador 1': randint(1,6), 'Jogador 2': randint(1,6), 'Jogador 3': randint(1,6), 'Jogador 4': randint(1,6)}
for i,v in jogadores.items():
    print(f'{i}° Teve O Resultado: {v}')
    sleep(1)
print('\nResultado Final:\n ')
for i in sorted(jogadores, key = jogadores.get, reverse = True):
    sleep(2)
    print(f'{cont+1}° Lugar {i} Com Resultado De {jogadores[i]} Pontos')
    cont = cont + 1 