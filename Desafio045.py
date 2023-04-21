#Crie um programa que faça o computador jogar Jokenpô com você.
import random
print(' '*50,'\033[33mBem Vindo Ao Jokenpô\033[m')
print('-'*140)
print('\033[31mFaça Sua Escolha:\033[m')
print('\033[32m[1] - Papel\n[2] - Tesoura\n[3] - Pedra\033[m')
usuario = int(input())
lista = ['Papel.','Tesoura.','Pedra.']
pc = random.choice(lista)


if(usuario == 1):
    print('\033[34mSua Escolha Foi:\033[m Papel.')
    print('\033[33mA Escolha Do Computador Foi:\033[m {}'.format(pc))
elif(usuario == 2):
    print('\033[34mSua Escolha Foi:\033[m Tesoura.')
    print('\033[33mA Escolha Do Computador Foi:\033[m {}'.format(pc))
elif(usuario == 3):
    print('\033[34mSua Escolha Foi:\033[m Pedra.')
    print('\033[33mA Escolha Do Computador Foi:\033[m {}'.format(pc))
elif(usuario < 1 or usuario >3):
    print('\033[7;31;41mOpção Invalida.\033[m')

if(pc == 'Papel.' and usuario == 1 or pc == 'Tesoura.' and usuario == 2 or pc == 'Pedra.' and usuario == 3):
    print('\033[35mNão A Vencedor, Temos Um Empate!\033[m')
elif(pc == 'Papel.' and usuario == 2):
    print('\033[32mVocê Venceu!\033[m')
elif(pc =='Papel.' and usuario == 3 ):
    print ('\033[31mO Computador Venceu!\033[m')
elif(pc=='Tesoura.' and usuario == 3 ):
    print('\033[32mVocê Venceu!\033[m')
elif(pc == 'Tesoura.' and usuario == 1 ):
    print ('\033[31mO Computador Venceu!\033[m')
elif(pc == 'Pedra.' and usuario == 1 ):
     print('\033[32mVocê Venceu!\033[m')
elif(pc == 'Pedra.' and usuario == 2):
    print ('\033[31mO Computador Venceu!\033[m')