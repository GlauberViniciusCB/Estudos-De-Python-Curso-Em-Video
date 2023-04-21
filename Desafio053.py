# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de 
# palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite Uma Frase: ')).strip().upper()
separando_palavras = frase.split()
junto_palavras = ''.join(separando_palavras)
inverso = ''
print('\n')
for letras in range (len(junto_palavras)-1,-1,-1):
        inverso = inverso + junto_palavras[letras]
if(junto_palavras == inverso):
    print('A Frase Digitada Foi: {}'.format(junto_palavras))
    print('O Inverso Da Frase É: {}'.format(inverso))
    print('\nA Frase Digitada  É Um Palíndromo!')
else:
    print('A Frase Digitada Foi: {}'.format(junto_palavras))
    print('O Inverso Da Frase É: {}'.format(inverso))
    print('\nA Frase Digitada Não É Um Palíndromo!')
