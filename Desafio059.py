# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

escolha = 0
num1 = int(input('Informe O 1° Número: '))
num2 = int(input('Informe O 2° Número: ')) 
while(escolha!=5):
    print('\n------ Menu ------')
    print('\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos Números\n[5] - Sair Do Programa\n')
    escolha = int (input('Faça Sua Escolha:'))
    if(escolha == 1):
        total = num1+ num2
        print('\nSua Escolha Foi Soma, Que Resulta Em: {} '.format(total))
    elif(escolha == 2):
        total = num1*num2
        print('\nSua Escolha Foi Multiplicação, Que Resulta Em: {}'.format(total))
    elif(escolha == 3): 
        print('\nSua Escolha Foi Qual É Maior Número? Que Resulta Em:')
        if(num1 > num2):
            print('{} É Maior Que {}'.format(num1,num2))
        elif(num2 > num1):
            print('{} É Maior Que {}'.format(num2,num1))
        else:
            print('Os Números São Iguais.')
    elif(escolha == 4):
        print('Então, Você Deseja Escolher Novos Números:')
        num1 = int(input('\nInforme O 1° Número: '))
        num2 = int(input('Informe O 2° Número: ')) 
    elif(escolha == 5):
        print ('Fim da execução')
    else:
        print('Opção Inválida!')