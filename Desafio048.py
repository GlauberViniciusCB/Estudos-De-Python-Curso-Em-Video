#Faça um programa que calcule a soma dos números impares entre todos os números que são múltiplos de três e que se encontram no 
#intervalo de 1 até 500.
soma = 0
cont = 0

for numeros in range (1,501):
    if(numeros % 2 == 1):
        if(numeros % 3 == 0):
            soma = soma + numeros
            cont = cont + 1    
print('\n\033[32mO Total De Números Impares No Intervalo Solicitado É {} E A  Soma Totaliza: {} \033[m'.format(cont,soma))