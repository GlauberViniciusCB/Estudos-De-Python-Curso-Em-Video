# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a 
# digitação novamente até ter um valor correto.

sexo = str(input('\nInforme Um Sexo:\nM - Masculino\nF - Feminino\n')).upper().strip()[0]
if(sexo!='M' and sexo!='F'):
    print('Escolha Inválida!')
    while(sexo !='M' and sexo !='F'):
        sexo= str(input('\nInforme Um Sexo:\nM - Masculino\nF - Feminino\n' )).upper().strip()[0]
print('\nEscolha Válida: {}'.format(sexo))

