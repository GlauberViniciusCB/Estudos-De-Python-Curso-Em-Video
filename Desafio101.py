# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date
def voto (idad):
    if(idad >= 18 and idad < 70):
        return (f'Você Tem {idad} Anos E Seu Voto É Obrigatório!')
    elif(idad < 18 and idad >= 16 or idade >= 65):
        return(f'Você Tem {idad} Anos E Seu Voto É Opcional!')
    else:
        return(f'Você Tem {idad} Anos E Seu Voto Foi Negado, Você Ainda Não Pode Votar!')




ano_atual = date.today().year
ano_de_nascimento = int(input('Digite O Ano De Nascimento: ')) 
idade = ano_atual -ano_de_nascimento
print(voto(idade)) 