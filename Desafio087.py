#  Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão 
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

lista = []
jogo =  [] 
total_de_jogos = 0
quant = int(input('Quantos Jogos Você Deseja Gerar ? '))
while (total_de_jogos < quant):
    cont = 0 
    while True:
        num = randint(1,60)
        if(num not in lista):
            lista.append(num)
            cont = cont + 1 
        if(cont == 6):    
             break
        lista.sort()
        jogo.append(lista[:])
        lista.clear()
    total_de_jogos = total_de_jogos + 1
print(jogo)
