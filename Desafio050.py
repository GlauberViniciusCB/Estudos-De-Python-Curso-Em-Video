#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor 
#digitado for ímpar, desconsidere-o.
soma = 0 ; cont = 0
for numeros in range (1,7):
    num = int(input('Digite O {}° Valor: '.format(numeros)))
    if(num % 2 == 0):
        soma= soma + num
        cont= cont +1 
print('\n\033[32mForam Informados {} Pares E A Soma Dos Números É: \033[m{}'.format(cont,soma))

