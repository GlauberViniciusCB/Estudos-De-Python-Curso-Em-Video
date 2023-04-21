# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('\n')
for numeros in range (1,51):
    if (numeros % 2 == 0):
        print(numeros, end =' ')
print('\nFim!')