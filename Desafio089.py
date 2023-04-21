# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o 
# conteúdo da estrutura na tela.
analise = {}
dados = []
analise['Nome']= str (input('Nome Do Aluno: '))
analise['Média'] = float(input('Qual Foi A Média Do Aluno: '))
if(analise['Média'] < 5):
    resultado = 'Reprovado'
elif(analise['Média']>= 5 and analise['Média']< 7):
    resultado = 'Recuperação'
else:
    resultado = 'Aprovado'
analise['Resultado Final'] = resultado
print('\n')
for i,v in analise.items():
    print(f'{i} = {v}')