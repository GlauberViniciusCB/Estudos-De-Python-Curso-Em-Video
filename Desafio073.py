# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de 
# colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense

times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará','Atlético-GO' ,'Avaí','Juventude')

print(f'\nOs 5 Primeiros Time: {times[:5]}')

print(f'\nOs Últimos 4 Colocados: {times[-4:]}')

print(f'\nO Times Em Ordem Alfabética: {sorted(times)}')

print('\nA Chapecoense Disputou Este Campeonato:','Chapecoense' in times)



