# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
i = 0
tupla = (int(input(f'Informe O {i+1}° Número: ')),int(input(f'Informe O {i+1}° Número: ')),int(input(f'Informe O {i+1}° Número: ')),int(input(f'Informe O {i+1}° Número: ')))

print('\n')
print(f'\nOs Elmentos Digitados Na Tupla Foram: {tupla}')
print(f'\nQuantas Vezes Apareceu O Valor 9 : {tupla.count(9)} Vezes')
if('3'in tupla):   
    print(f'\nEm Que Posição Foi Digitado O Primeiro Valor 3: {tupla.index(3)}')
else:
    print(f'\nNão Há O Número 3 Entre Os Valores Digitados Na Tupla.')
print(f'\nOs Números Pares Digitados Foram : ',end='')
for num in tupla:
    if(num % 2 == 0):
        print(num,end=' ')