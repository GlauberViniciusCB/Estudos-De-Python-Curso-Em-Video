# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter 
# apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas 
# geradas
numeros = []
pares = []
impar = []
while True:
    num = (int(input('Informe Um Número: ')))
    if(num %2 == 0):
        numeros.append(num)
        pares.append(num)
    else:
        numeros.append(num)
        impar.append(num)
    esc = str(input('Deseja Continuar Informando Valores: [S/N] ')).upper()
    while(esc != 'N' and esc != 'S'):
         esc = str(input('Só Aceitamos [S/N] Como Resposta: ')).upper()
    if(esc == 'N' ):
        print(f'\nA Lista Com Todos Os Elementos: {numeros}')
        print(f'Lista Só Com Elemento Pares: {pares}')
        print(f'Lista Só Com Elemento Impares: {impar}')
        break

