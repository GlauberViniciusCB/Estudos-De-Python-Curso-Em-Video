# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
dados = {}
pessoas = [] 
cont_p = 0
media = 0
somaid = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Informe O Nome: '))
    cont_p = cont_p + 1
    dados['Sexo'] = str(input('Informe  O Sexo: ')).upper()
    if(dados['Sexo']!= 'M'and dados['Sexo'] !='F'):
        print('Por Favor, Informe Um Opção Válida [F/M]')
        while(dados['Sexo'] != 'M'and dados['Sexo'] != 'F'):
             dados['Sexo'] = str(input('Informe O Sexo: ')).upper()
    dados['Idade'] = int(input('Informe A Idade: '))
    somaid = somaid + dados['Idade'] 
    pessoas.append(dados.copy())
    esc = str(input('Deseja Continuar: [S/N] ')).upper()
    if(esc != 'S' and esc != 'N'):
        print('Opção Inválida, Escolha Entre "S" E "N"')
        while(esc != 'S' and esc != 'N'):
            esc = str(input('Deseja Continuar: [S/N] ')).upper()
    if(esc ==  'N'):
        print(dados)
        break    
media = somaid/cont_p 
print(pessoas)
print(f'Foram Cadastradas {cont_p} Pessoas.')
print(f'A Média De Idade É: {media:.2f} ')
print(f'As Mulheres Presentes Na Lista São: ',end= '')
for i in pessoas:
    if (i["Sexo"] == 'F'):
        print(f'{i["Nome"]}', end = ',')
print(f'\nAs Pessoas De Idade Superior A Media São:', end= ',')
for j in pessoas:
    if(j["Idade"]>= media):
        print(f'{j["Nome"]}',end= ',')