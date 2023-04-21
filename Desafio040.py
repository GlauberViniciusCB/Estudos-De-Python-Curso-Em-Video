# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com 
# a média atingida:
nota1 = float(input('Informe A Sua 1° Nota: '))
nota2 = float(input('Informe A Sua 2° Nota: ')) 
media = float(nota1+nota2)/2
print('Sua Media Final É: \033[35m{}\033[m'.format(media))

if( media < 5.0 ):
    print('\033[31mVocê Foi Reprovado !\033[m')
elif(media >= 5.0 and media <= 6.9 ):
    print('\033[33mVocê Esta De Recuperação !\033[m')
else:
    print('\033[32mParabens,Você Foi Aprovado !\033[m')