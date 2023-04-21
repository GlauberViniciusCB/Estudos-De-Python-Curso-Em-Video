# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar 
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
cont = 0
escolha_pc= randint(0,10)
escolha_user = int(input('\nQual O Número Entre 0 E 10 Foi Escolido Pelo Computador? '))
if(escolha_pc != escolha_user):
    while(escolha_pc != escolha_user):
        print('\n\033[31mVocê Errou Tente Novamente.\033[m')
        escolha_user = int(input('\nQual O Número Entre 0 E 10 Foi Escolido Pelo Computador? '))
        cont =cont+1
print('\033[32mVocê Acertou O Número Digitado Foi:\033[m {} '.format(escolha_pc))
print('\033[33mForam Necessárias:\033[m {} \033[33mTentativas.\033[m'.format(cont))