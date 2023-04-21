import random
aluno1 = str (input('Informe O Nome Do Primeiro Aluno: '))
aluno2 = str (input('Informe O Nome Do Segundo Aluno: '))
aluno3 = str (input('Informe O Nome Do Terceiro Aluno: '))
aluno4 = str (input('Informe O Nome Do Quarto Aluno: '))

lista_de_alunos = (aluno1,aluno2,aluno3,aluno4)
escolha = random.choice(lista_de_alunos)
print('O Aluno Sorteado, Para Apagar O Quadro Foi: {} '.format(escolha))