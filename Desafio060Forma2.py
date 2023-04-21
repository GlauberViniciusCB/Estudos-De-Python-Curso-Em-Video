num = int(input('Informe Um Número:'))
fatorial = 1
for cont in range(num,0,-1):
    print(cont,end= ' ')
    fatorial = fatorial*cont
print('O Fatorial De {}! É Igual A {} '.format(num,fatorial))
