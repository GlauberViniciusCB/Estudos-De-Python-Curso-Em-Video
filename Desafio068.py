# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando 
# o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
cont = 0
seq_ganho = 0
while True:   
    cont = cont + 1
    Pc_esc =  ' '
    minha_esc = str(input('\nFaça Sua Escolha: \n[P] - Par\n[I] - Ímpar\n')).upper()
    if(minha_esc == 'P'):
        Pc_esc = 'I'
    if(minha_esc == 'I'):
        Pc_esc = 'P'
    minha_quant = int(input('Qual A Quantidade Você Vai Jogar? '))
    pc_quant = randint(0,10)
    print(f'O Pc Jogou :{pc_quant}')
    soma = minha_quant + pc_quant
    print(f'O Resultado: {soma}')
    if(soma % 2 == 0):
        resultado = 'P'
        print('Par Venceu!')
    elif(soma % 2 != 0):
        resultado = 'I'
        print('Impar Venceu!')
    if(resultado == minha_esc ):
        print('\033[32mVocê Venceu!\033[m')
    elif(resultado != minha_esc):
        print('\033[31mO Computador Venceu!\033[m')
    if(resultado != minha_esc):
        seq_ganho = cont-1
        print(f'\033[33mVocê Conseguiu Vencer {seq_ganho} Vezes Consecutivas.\033[m')
        break