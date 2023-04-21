# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
# guardado
# em um dicionário, incluindo o total de gols feitos durante o campeonato.
# Aprimore o desafio para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do 
# aproveitamento de cada jogador.
jogador = {}
gols= []
time = []
while True:
    gols.clear()
    jogador['Nome'] = str(input('Nome: '))
    quant = int(input(f'Quantas Partidas Jogou {jogador["Nome"]}? '))
    for gol in range (quant):
        gols.append(int(input(f'Quantos Gols Na {gol+1}° Partida? ')))
        jogador['Gols Por Partida'] = gols[:]
        jogador['     Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        esc = str(input('Deseja Continar? [S/N] ')).upper()[0]
        if(esc in  'SN'):
            break
        print('Opção Invalida.')
    if(esc == 'N'):
        print('Ok! Você Não Quer Mais Adicionar Ninguém')
        break
print('\n')
for k in jogador.keys():
    print(f'{k:<15}',end='')
print()
for k,v in enumerate(time):
    print(f'{k+1:>5}° ',end='')
    for valor in v.values():
        print(f'{str(valor):<15} ',end='') 
    print()
while True:
    dados = int(input('Deseja Ver Os Dados De Qual Jogador, Digite (999) Para Parar: '))
    if(dados == 999):
        break 
    if(dados >= len(time)):
        print("ERRO! Esse Jogador Não Existe")
    else:
        print(f'Estatisticas do Jogador{time[dados]["Nome"]} ')
        for num,jog in enumerate((time[dados+1]["Gols Por Partida"])):
            print(f'{num+1}° Jogo Marcou {jog} Gols.')
  

        