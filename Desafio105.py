# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
# as seguintes informações:

# – Quantidade de notas                                                                                                                                                  – A maior nota                                                                                                                                                                – A menor nota                                                                                                                                                              – A média da turma                                                                                                                                                      – A situação (opcional)

# – A maior nota 
# – A menor nota   
# – A média da turma   
# – A situação (opcional)

def notas(*n,sit=0):
    nota = {}
    nota['Total De Notas'] = len(n) 
    nota['Maior Nota'] = max(n)
    nota['Menor Nota'] = min (n)
    media = sum(n)/len(n)
    nota['Media Das Notas'] = media
    if(sit == True):
        if(nota['Media Das Notas']<= 5):
            nota['Situação'] = 'A Situação É Ruim!'
        elif(nota['Media Das Notas'] > 5 and nota['Media Das Notas'] < 7):
            nota['Situação'] = 'A Situação É Razoavel' 
        else:
            nota['Media Das Notas'] = 'A Situação É Boa!'
    # return print(nota)
    for i in nota.items():
        print(i)
notas(2.6,5.7,10,sit= True)