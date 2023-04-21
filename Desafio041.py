# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua 
# categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

atual = date.today().year
ano_de_nasc = int(input('\033[33mEm Qual Ano Você Nasceu?\033[m'))
idade = atual - ano_de_nasc

print('\033[32mVocê Tem {} Anos!\033[m'.format(idade))
if( idade <= 9):
    print('E Pertence A Categoria \033[33mMirim\033[m.')
elif(idade > 9 and idade <= 14 ):
    print('E Pertence A Categoria \033[33mInfantil\033[m.')
elif(idade > 14 and idade <= 19):
    print('E Pertece A Categoria \033[34mJunior\033[m.')
elif(idade == 20 ):
    print('E Pertece A Categoria \033[35mSênior\033[m.')
else:
    print('E Pertece A Categoria \033[31mMaster\033[m.')
