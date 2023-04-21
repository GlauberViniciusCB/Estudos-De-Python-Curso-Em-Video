# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:                       
# A) Quantos números foram digitados.                                                       
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.
numero =[] 
while True:
    numero.append(int(input('Informe  Um Número: ')))
    esc = str(input('Deseja Continuar Inserindo Valores: [S/N] ')).upper()
    while(esc != 'N' and esc !='S'):
        esc = str(input('Por Favor Escolha Entre [S/N], Deseja Continuar Inserindo Valores: [S/N] ')).upper()
    if(esc == 'N'):
        print(f'\nA Lista De Elemento Digitados Contém Os Seguintes Elementos: {numero}.')
        print (f'Tem O Total De {len(numero)} Elementos.')
        numero.sort(reverse=True)
        print(f'Lista Ordenada Em Forma Descrescente: {numero}')
        if (5 not in numero):
            print(f'O Valor 5 Não Aparece Na Lista.')
        else:
            print(f'O Valor 5 Aparece na Posição {numero.index(5)} .')
        break
