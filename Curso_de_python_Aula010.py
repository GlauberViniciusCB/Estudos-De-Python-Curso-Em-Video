# Tempo = int(input('Quantos Anos Tem O Seu Carro ? '))
# if(Tempo <=3):
#     print('Seu Carro É Novo!')
# else:
# #     print('Seu Carro É Velho!')

# nome = str(input('Qual É O Seu Nome? ')).strip()
# if (nome == 'Glauber'):
#     print('Que Nome Legal!')
# else :
#     print('Seu Nome É Tão Normal!')
# print('Bom Dia, {}!'.format(nome)) 

nota1 = float(input('Informe A Nota Da 1° Prova: '))
nota2 = float(input('Informe A Nota Da 2° Prova: '))
media = (nota1+ nota2)/2
if(media<6):
    print('{:.2f} Sua Nota Está Abaixo Do Esperado, Você Está Reprovado!'.format(media))
else:
    print('Sua Média Final É {:.2f}, Você Está Aprovado!'.format(media))