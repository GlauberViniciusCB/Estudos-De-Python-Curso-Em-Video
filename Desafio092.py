# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador= {}
total_gols = 0
cada_part = []
jogador['Nome'] = str(input('Informe O Nome Do Jogador: '))
quant_part= int (input(f'Quantas Partidas {jogador["Nome"]} Disputou? '))
for _ in range(quant_part):
    gol_part = int(input(f'Quantos Gols Foram Marcados Na {_+1}° Partida: '))
    total_gols = gol_part + total_gols 
    cada_part.append(gol_part)
    jogador['Total Gols No Campeonato'] = total_gols 
    jogador['Gols Por Partida'] = cada_part

print(f'Nome: {jogador["Nome"]}')
print(f'Gol Por Partida: {jogador["Gols Por Partida"]} ')
print (f'Total De Gols No Campeonato: {jogador["Total Gols No Campeonato"]} ')
print('\n')
print(jogador)
print('\n')
for n,i in enumerate(cada_part):
    print(f'{jogador["Nome"]} Marcou Na {n+1}° Partida {i} Gol(s).')