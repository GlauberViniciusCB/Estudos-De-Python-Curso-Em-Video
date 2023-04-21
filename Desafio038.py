# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int (input('\033[33mInforme Um Número:\033[m '))
n2 = int (input('\033[33mInfome Outro Número:\033[m '))

if(n1 > n2):
    print('\033[32mO Primeiro Valor É Maior.\033[m')
elif(n2 > n1):
    print('\033[32mO Segundo Valor É Maior\033[m')
else:
    print('\033[31mNão Exite Valor Maior, Os Dois Números São Iguais.\033[m')