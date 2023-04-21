# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando 
# o total de vitórias consecutivas que ele conquistou no final do jogo. 
from  random import randint
pc_escolha = ' '
user_escolha = ' '
# user_escolha = str(input('\nFaça A Sua Escolha \n\033[33m[I]- Ímpar Ou [P] Par.\033[m\n')).strip().upper()
if(user_escolha != 'I' or user_escolha != 'P' ):
    user_escolha = str(input('\nFaça A Sua Escolha \n\033[33m[I]- Ímpar Ou [P] Par.\033[m\n')).strip().upper()
    while (user_escolha != 'I' and user_escolha != 'P'):
        print('\033[31mPor Favor, Faça Uma Escolha Entre: \033[33m[I]- Ímpar Ou [P] Par: \033[m')  
        user_escolha = str(input('Faça A Sua Escolha: \n\033[33m[I]- Ímpar Ou [P] Par.\033[m\n')).upper().strip()
        if(user_escolha == 'I' or user_escolha =='P' ):
            break
        if(user_escolha == 'P'):
            pc_escolha = 'I'
        elif(user_escolha == 'I'):
            pc_escolha = 'P'
        quant_user = 0
        quan_user = int (input('Escolha Um Número Entre 1 E 10 Para Jogar: '))
        if(quan_user < 0 or quan_user > 10):
            while True:
                if(quan_user < 0 or quan_user > 10):
                    quan_user = int (input(f'\033[34mFaça Sua Escolha Novamente, Não É Possivel Jogar {quan_user}, Digite Um Número Entre 1 E 10 Para Jogar? \033[m '))
            # if(quan_user < 0 or quan_user > 10):
                    # quant_user =int(input(f'\033[31mPor Favor! Não Insista Em Jogar O Valor {quan_user}, Ele Esta Fora Dos Padrões.Faça A Escolha Certa:\033[m '))
            # elif(quant_user >=0 and quant_user<=10):
                else:
                    break
        if(quan_user >=0 and quan_user<=10):
                soma = 0
                quant_pc = randint(0,10)  #escolha do pc 
                soma = quan_user + quant_pc
                print(quant_pc)
                print(quan_user)
                print(soma)
                if(soma % 2 == 0):
                    resultado = 'Par Venceu!'
                    print(resultado)
                elif(soma % 2!= 0):
                    resultado = 'Ímpar Venceu!'
                    print(resultado)