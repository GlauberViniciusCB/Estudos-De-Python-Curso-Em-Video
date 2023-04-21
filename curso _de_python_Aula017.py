num = [3,2,34,8,9]
print(f'{num}')
num[2] = 3 
print(f'Lista Alterando O Indice[2]: {num}')
num.append(7)
print(num)
num.sort()
print(f'Lista Ordenada: {num}')
num.sort(reverse= True)
print(f'Lista Na Ordem Decrescente{num}')
print(f'Esta Lista Tem {len(num)} Elementos.')
if (8 in num):
    num.remove(8)
    print(num)
else:
    print('A Lista Não Tem O Número "4".')