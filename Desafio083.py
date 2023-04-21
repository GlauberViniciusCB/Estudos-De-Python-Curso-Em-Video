# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas.     
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.
pessoas = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(str(input('Informe Um Nome: ')))
    dados.append(float(input('Digite Um Peso: ')))
    if(len(pessoas) == 0):
        maior = dados[1]
        menor = dados[1]
    else:
        if(dados[1] > maior ):
            maior = dados[1]
        if(dados[1]< menor):
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    esc = (str(input('Você Deseja Continuar: [S/N]'))).upper()
    if(esc == 'N'):
        print(f'Foram Cadastradas {len(pessoas)}')
        for i in pessoas:
            if(i[1] == maior):
                print(f'A Pessoa Com o Maior Peso É: {i[0]}')
            if(i[1] == menor):
                print(f'A Pessoa Com o Menor Peso É: {i[0]}') 
        print(f'Maior Peso É {maior} E Menor É {menor}.')
        break
