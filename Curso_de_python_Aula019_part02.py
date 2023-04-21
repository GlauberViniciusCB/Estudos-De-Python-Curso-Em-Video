pessoas = {'Nome':'Glauber','Idade':'23','Sexo':'M'}
pessoas['Peso'] = 62.2
# for k in pessoas.keys():
#     print(k)
print('\n')
# for k in pessoas.values():
#     print(k)
# del pessoas['Sexo']
for k,v in pessoas.items():
    print(f'{k} = {v}')
