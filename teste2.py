# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

# n = int(input('Informe Um Número: '))
# cont = 2
# termo1 = 0
# termo2 = 1
# print(termo1,end= ' -> ')
# print(termo2,end= ' -> ')
# while( cont < n):
#     soma = termo1 +termo2
#     termo1 = termo2 
#     termo2 = soma
#     cont = cont +1
#     if(cont==n ):
#        print(soma,end=' ')
#     else:
#         print(soma,end=' -> ')
#     # if(cont==n ):
#     #     print(end='')
#     # else:
#     #     print(end=' - ')

# matriz =[[0,0,0],[0,0,0],[0,0,0]]
# for i in range (0,3):
#     for j in range(0,3):
#         matriz[i][j] = int(input('Informe Um Número: '))
# for i in range (0,3):
#     for j in range (0,3):
#         print(matriz[i][j], end = ' ')
#     print() 

print('Defeitos:\n1 - Necessita de Esfera\n2 - Necessita de limpeza\n3 - Necessita troca de cabo ou conector\n4 - Quebrado ou inutilizado')
defeitos_ = ['Necessita de Esfera','Necessita de limpeza','Necessita troca de cabo ou conector','Quebrado ou inutilizado']


num_mouses = int(input('Quantos mouses defeituosos exeistem: '))
defeitos = 4*[0]

print('')
for idx in range(num_mouses):
    
    validacao = True
    while validacao:
        defeito = int(input('Qual o código do problema do mouse '+str(idx+1)+': '))
        if (defeito == 1) or (defeito == 2) or (defeito == 3) or (defeito == 4):
            validacao = False
        else:
            print('Número inválido, tente outro!')
    defeitos[defeito-1] = defeitos[defeito-1] + 1

for idx in range(len(defeitos_)):
    print(defeitos_[idx]+' - ' +str(defeitos[idx])+ 'defeitos - ' +str(defeitos[idx]*100/num_mouses)+'%' )
 