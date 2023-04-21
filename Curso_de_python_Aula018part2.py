# galera = [['João',19],['Ana',33],['Joaquim',13],['Maria', 45]]
# # print(galera[2][1])
# for i in galera:
#     print(f'{i[0]} Tem {i[1]} Anos.' )
##########################################################################

galera = [] 
dados =  []
totalMai= 0
totalMen = 0
for i in range (0,3):
    dados.append(str(input('Informe Um Nome: ')))
    dados.append(int(input('Informe A Idade: ')))
    galera.append(dados[:])                     #Joguei Os Dados Dentro Da Lista Galera.
    dados.clear()
print(galera)
print('\n')
for j in galera:
    if(j[1] >= 18):
        print(f'{j[0]} É Maior De Idade E Tem {j[1]} Anos.')
        totalMai = totalMai + 1
    else:
        print(f'{j[0]} É Menor De Idade Tem {j[1]} Anos.')
        totalMen = totalMen + 1 

print(f'Temos {totalMai} Pessoas Maior De Idade.')
print(f'Temos {totalMen} Pessoas Menor De Idade.')
