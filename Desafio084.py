# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
conteudo =[[],[]]
for n in range(0,7):
    num = (int(input(f'Informe O {n+1}° Número: ')))
    if(num % 2 == 0):
        conteudo[0].append(num)
    else:
        conteudo[1].append(num)

print(f'Os Valores Pares Ordenados São:{sorted(conteudo[0])}')
print(f'Os valores Impares Ordenados São:{sorted(conteudo[1])}')