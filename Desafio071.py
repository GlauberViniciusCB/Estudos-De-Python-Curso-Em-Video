# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a 
# ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('*='*45)
print('{:^90}'.format('CAIXA ELETRÔNICO '))
print('*='*45)
quant = int(input('Quanto Você Deseja Sacar: R$ '))        
total = quant 
nota = 50 
cont = 0
while True:
    if(total >= nota):
        total =  total - nota 
        cont  = cont + 1
    else:
        print(f'{cont} Notas De {nota}')
        if(nota == 50):
            nota = 20
        elif(nota == 20):
            nota = 10
        elif(nota == 10):
            nota = 1
        if(total == 0):
            break
        cont = 0