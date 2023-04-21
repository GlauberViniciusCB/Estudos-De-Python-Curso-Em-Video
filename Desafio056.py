# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
total_idade = 0
maior = 0
cont = 0
for i in range(1,5):
    nome =  str(input('\nInforme O Nome Da {}° Pessoa: '.format(i)))
    idade = int(input('Informe A Idade Da {}° Pessoa: '.format(i)))
    sexo =  str(input('Informe O Sexo Da {}° Pessoa (M) - Masculino (F) - Feminino : '.format(i))).upper()
    total_idade = total_idade+idade
    media_idade = total_idade/4
    if(sexo == 'M'):
         if(i == 1):
            maior = idade
            h_velho = nome
         else:
            if(idade > maior):
                maior = idade
                h_velho = nome
    if(sexo == 'F'):
        if(idade <20):
            cont= cont+1

print('\n')
print('A Média Das Idades Do Grupo: {}'.format(media_idade))
print('O Homem Mais Velho: {}'.format(h_velho))
print('A Quantidade De Mulheres Com Menos De Vinte Ano(s)): {} '.format(cont))