# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando 
# a estrutura while.

# formula: a1+(n-1)*R
cont=0
a1  = int(input('Informe O 1° Termo: '))
r   = int(input('Informe A Razão: '))
ult = a1+(10-1)*r
cont= a1
while(cont<ult):
    print(cont,end=' ')
    cont= cont +r
print('{} É A Progressão Aritmética Dos 10 Primeiros No Qual O  1° Termo É {} E A Razão {}. '.format(cont,a1,r)) 