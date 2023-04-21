soma = 0
while True:
    num = int(input('Informe Um Número: '))
    if(num == 999):
        break
    soma = soma + num
print('Acabou!')
print('A Soma É: {} '.format(soma))