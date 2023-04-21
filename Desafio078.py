# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor 
# digitado e as suas respectivas posições na lista. 
num = []
for numero in range(0,5):
    num.append(int(input(f'Informe O Número Da Posição {numero}: ')))
print(f'\nO Maior Número Da Lista É: {max(num)} E Está Na Posição: {num.index(max(num))}')
print(f'\nO Menor Número Da Lista É: {min(num)} E  Está Na  Posição: {num.index(min(num))}')
