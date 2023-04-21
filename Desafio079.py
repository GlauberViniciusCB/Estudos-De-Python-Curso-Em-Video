# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já 
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem 
# crescente. 
num = []
while True:
    n = (int(input('Informe Um Número: ')))
    if(n not in num):
        num.append(n)
    else:
        print('Este Número Já Está Presente Na Lista.')
    esc= str(input('Deseja Continuar Adicionando Elementos Na Lista: [S/N] ')).upper()
    while(esc != 'S' and esc !='N' ):
        print('Por Favor, Digite Um Resposta Válida S[Sim] Ou N[Não]. ') 
        esc= str(input('Deseja Continuar Adicionando Elmentos Na Lista: [S/N] ')).upper()
    if(esc =='N'):
        break
print(f'A Lista Tem Os Seguintes Elementos {num} ')
print(f'A Lista Ordenada {sorted(num)}')