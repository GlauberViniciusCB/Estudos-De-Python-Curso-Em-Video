frase = ('Estou Aprendendo Python')
print(frase[0:20:3])
escrito = ('Gláucio Felipe')
print(escrito[:5])

nome= ('Gleicyenne Beatriz')
print(nome[9:])


frase1 = 'Python não é dificil!'
print ('\nA Frase É Composta Por {} Caracteres.'.format(len(frase1)))
print('\nNa Frase Temos {} Letras I.'.format(frase1.count('i')))

print('\nA Conteúdo Pesquisado Começa A Partir Da Posição: {}.'.format(frase1.find('dif')))

print('\nPython' in frase1)

print(frase1.replace('Python','C++'))

print('\nTransformando A Frase1 Em Maiúsculo: {}'.format(frase1.upper()))

print('\nTransformando A Frase Em Minúsculo: {}'.format(frase1.lower()))

frase2 = 'glauber vinicius campos batista.' 
print('\nO 1° Caractere Fica Em Maiúsculo e o Resto Da frase Em Minusculo: {}'. format(frase2.capitalize() ))

print ('\nFaz A Quebra Da String, E Ao Encontrar Um Espaço Inicia Com A Letra Maiúscula: {}'.format(frase2.title()))
