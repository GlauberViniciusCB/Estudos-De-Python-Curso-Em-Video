#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite Um Frase: ')).strip().upper()
print ('A Letra A Aparece {} Vezes.'.format(frase.count('A')))
print('A Primeira Posição Que A Letra A Aparece É: {}'.format(frase.find('A')+1))
print('A Ultima Posição Que A Letra A Aparece É: {}'.format(frase.rfind('A')+1))