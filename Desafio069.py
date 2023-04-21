# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se 
# o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
print('=='*22,'SEJA BEM VINDO AO SISTEMA DE CADASTRO DE PESSOAS','=='*22)
cont = 1
cont_m_idade = 0
cont_masc = 0
cont_Fem = 0
while True: 
    idade = int(input(f'Informe A Idade Da {cont}° Pessoa: ').strip())
    if(idade > 18):
        cont_m_idade= cont_m_idade+1
    sexo  = str(input(f'Informe O Sexo Da {cont}° Pessoa [M/F]: ')).upper().strip()
    if(sexo != 'M' and sexo!= 'F'):
        print('\033[31mOpção Invalida Escolha: [M/F]\033[m')
        while(sexo != 'M' and sexo!= 'F'):
             sexo  = str(input(f'Informe O Sexo Da {cont}° Pessoa [M/F]: ')).upper().strip()
    cont = cont +1
    if(sexo == 'M'):
        cont_masc = cont_masc + 1
    if(sexo == 'F'and idade <20):
        cont_Fem = cont_Fem +1  
    esc = str(input('Você Deseja Continuar Cadastrando Pessoas? [S/N] ')).upper().strip()
    if(esc!='S' and esc!= 'N'):
        while(esc !='S' and esc!= 'N'):
            print('\033[31mOpçao Invalida\033[m')
            esc = str(input('Você Deseja Continuar Cadastrando Pessoas? [S/N] ')).upper().strip()
    if(esc=='N'):
        print('\n\033[33mPrograma Finalizado.\033[m\n')
        print(f'O Total De Pessoas Cadastradas Com Mais De 18 Anos É: {cont_m_idade} ')
        print(f'O Total De Homens Cadastrados Foi De: {cont_masc}')
        print(f'O Total De Mulheres Com Menos De 20 Anos É De: {cont_Fem} ')
        break