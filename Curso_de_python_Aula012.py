nome = str(input ('\033[33mQual É O Seu Nome:\033[m ')).strip()
if (nome == 'Glauber'):
    print('Olá Glauber, Que Nome Legal!')
elif(nome == 'João' or nome == 'Maria' or nome == 'José' or nome == 'Ana' ):
    print('Seu Nome É Bem Popular No Brasil.')
elif (nome in 'Gláucio Gleicyenne'): #Em Nome Tem As Palavras Gláucio E Gleicyenne.
    print('Legal, Seu Nome É Bem Diferente.')
else:
    print('Seu Nome É Tão Comum!')
print ('\033[32mBom Dia, {}!\033[m'.format(nome))