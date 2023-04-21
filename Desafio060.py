# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# num = int(input('Informe Um Número: ')) 
num = int(input('Calcule A Fatorial Do Número : '))
cont= num
f = 1
while(cont > 0):
    print(cont,end=' ')
    f= cont*f
    cont = cont -1 
print('= {}'.format(f))     

