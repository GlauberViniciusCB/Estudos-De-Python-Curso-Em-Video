# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu 
# programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    num = int(input('Informe Um Número Inteiro Entre 0 e 20: '))
    while(num > 20 or num < 0):
       print('\033[31mTente Novamente!\033[m')
       num = int(input('Informe Um Número Inteiro Entre 0 e 20: ')) 
    print(f'O Número {num} Escrito Por Extenso É: {numeros[num]}')
    esc = str(input('Você Deseja Continuar?[S/N]')).upper()
    if(esc  == 'N'):
        break
