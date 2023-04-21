# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa 
# progressão.

num = int(input('Informe O 1° Termo: '))
razao = int(input('Informe A Razão: '))
ultimo = num +( 10 - 1)*razao
print('\n\033[33mA Progressão Aritmética Dos \033[m10 \033[33mPrimeiros 10° Termos Do Número: \033[m{}\033[33m De Razão \033[m{} \033[33mSão:\033[m'.format(num,razao),end=' ')
for i in range(num,ultimo+razao,razao):
    print(i,end=' ') 
print('\n')
