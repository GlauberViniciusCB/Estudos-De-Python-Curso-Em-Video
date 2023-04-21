#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de 
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Informe Um Número Inteiro: '))
opcao = int(input('Informe A Base Que Deseja Converter O Número: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\n '))

if(opcao < 1 or opcao > 3):
    print('Opção Invalida!')
elif(opcao == 1):
    conv = bin(num)
    print('O Número {} Convertido Para Binário É: {}'.format(num,conv[2:]))
elif(opcao == 2):
    conv = oct(num)
    print('o Número {} Convertido Para Octal É: {}'.format(num,conv[2:]))
elif(opcao == 3):
    conv = hex(num)
    print('O Número {} Convertido Para Hexadecimal É: {}'.format(num,conv[2:]))

