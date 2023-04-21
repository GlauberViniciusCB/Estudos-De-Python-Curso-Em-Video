# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se 
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também
# deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
nasc = int(input('\033[33mInforme O Seu Ano De Nascimento:\033[m '))
sexo = str(input('\033[33mQual O Seu Sexo:\n[M]- Masculino\n[F]- Feminino\033[m\n')).upper()
ida = ano_atual -nasc
print('\033[32mVocê Tem {} Anos.\033[m'.format(ida))
if(sexo == 'F'):
    print('Você Não Precisa Se Alistar!')
elif(sexo == 'M'):
    if((ano_atual - nasc) > 18):
        idade = (ano_atual - nasc) - 18
        print('\033[31mJá Passou Da Hora De Se Alistar No Serviço Militar. Você Está Atrassado Em {} Anos\033[m'.format(idade))
    elif((ano_atual - nasc) == 18):
        print('\033[36mEstá Na Hora De Se Alistar No Serviço Militar.\033[m')
    else:
        idade = 18 - (ano_atual - nasc) 
        print('\033[32mVocê Ainda Não Precisa Se Alistar No Serviço Militar. Ainda Falta {} Anos Para Se Alistar.\033[m'.format(idade))
elif(sexo != 'F' and sexo != 'M' ):
    print('\033[31mEste Sexo Não Exite, Por Favor Escolha\033[32m M\033[m Ou \033[32mF\033[m!')