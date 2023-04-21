#  Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#  O programa será interrompido quando o número solicitado for negativo.
while True:
    print('\033[33mPara Encerrar Digite Um Número Menor Que Zero: \033[m')
    num = int(input('Informe O Número Que Deseja Ver A Tabuada: '))
    if(num < 0):
        print('\033[34mVocê Finalizou O Programa.\033[m')
        break
    i = 1
    while(i <= 10):
        total = num * i
        print(f'{num} X {i} = {total}') 
        i = i + 1
    