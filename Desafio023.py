num = int(input('Informe Um Numero Inteiro De 0 A 9999:'))
print('\nAnalise Do Número: {}'.format(num))
u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000%10 
print('{} - Unidades'.format(u))
print('{} - Dezenas '.format(d))
print('{} - Centenas'.format(c))
print('{} - Milhar'  .format(m))
