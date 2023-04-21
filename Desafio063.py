# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de 
# Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
n = int (input('Informe A Quantidade De Termos Que Deseja Ver Da Sequência De Fibonacci: '))
termo1 = 0
termo2 = 1 
cont = 2 
print(termo1,end = ' - ')
print(termo2,end = ' - ')
while(cont < n):
    soma = termo1 + termo2
    termo1 = termo2
    termo2 = soma
    cont = cont+1  
    if(cont == n):
        print(soma,end='')
    else:
        print(soma,end= ' - ')
  