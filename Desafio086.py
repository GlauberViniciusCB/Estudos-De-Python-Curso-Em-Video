# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz= [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
somaterc = 0
maior = 0
for i in range (0,3):
    for j in range (0,3):
        matriz[i] [j] = int(input('Informe Um Número: '))
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]}]', end=' ')
        if(matriz[i][j] % 2==0):
            soma= soma + matriz[i][j]
    print()
print(f'A Soma De Todos Os Valores Pares É: {soma}')
for i in range(0,3):
    somaterc = somaterc + matriz[i][2]
print(f'A Soma Da Terceita Coluna É: {somaterc}')

for j in range (0,3):
    if(i == 0):
        maior= matriz[1][j]
    else:
        if(matriz[1][j] > maior):
            maior = matriz[1][j]
print(f'O Maior Elemento Da Segunda Linha É {maior} ')



