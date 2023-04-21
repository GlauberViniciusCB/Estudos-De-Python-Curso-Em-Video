# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e 
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
atual = date.today().year
dados= {}

dados['Nome'] = str(input('Nome: '))
Ano_De_Nascimento = int(input('Ano De Nascimento: '))
dados['Idade'] = atual - Ano_De_Nascimento
dados['Carteira De Trabalho'] = int(input('Informe O Número Da Carteira De Trabalho: Caso Não Tenha Digite "0" '))
if(dados['Carteira De Trabalho'] != 0):
    dados['Ano De Contratção'] = int(input('Informe O Ano Da Sua Contratação: '))
    dados['Salário'] = float(input('Informe O Seu Salário: R$'))
    apos_idade = dados['Ano De Contratção']  - Ano_De_Nascimento
    apos_idade = apos_idade + 35 
    dados['Idade Que Vai Aposentar']= apos_idade
if(dados['Carteira De Trabalho'] == 0):
    dados['Carteira De Trabalho'] = 'Você Não Possui Carteira De Trabalho.'
print('\nINFORMAÇÕES GERAIS:\n')
for i,v in dados.items():
    print(f'{i}: {v}')