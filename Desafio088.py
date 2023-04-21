# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um 
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
while True:
        nome = str(input('Informe Um Nome: '))
        nota_1 = float(input('Informe A 1° Nota: '))
        nota_2 = float(input('Informe A 2° Nota: '))
        media = (nota_1 + nota_2)/2
        esc = str(input('Deseja Adicionar Mais Alunos [S/N]: ')).upper()
        alunos.append([nome,[nota_1,nota_2],media])
        if(esc == 'N'):
                break
print('\n')
for cont,i in enumerate(alunos):
        print(f'{cont}° Aluno: {i[0]} Média Final: {i[2]:.1f}')
while True:
        ver_nota = int(input('\nVocê Quer Ver As Notas De Qual Aluno? (Digite - Para Interromper)'))
        if(ver_nota == 1000):
                break
        if(ver_nota <= len(alunos)-1):
                print(f'\nO Aluno: {alunos[ver_nota][0]} Teve As Notas: {alunos[ver_nota][1]}')
        
