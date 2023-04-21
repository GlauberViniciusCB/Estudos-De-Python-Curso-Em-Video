#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int (input('Informe O Número Que Deseja Ver A Tabuada:'))
print('='*11)
for i in range (1,11):
    for j in range (1,11):
        resultado = i*n
    print('{:^1} X {:^1} = {}'.format(n,i,resultado))
print('='*11)

