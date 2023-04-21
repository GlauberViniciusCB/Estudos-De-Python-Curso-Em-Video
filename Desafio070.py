# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou 
# não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 
soma = 0
cont = 0
cont_1000 = 0
m_barato = ' ' 
while True: 
    nome =  str(input('Qual É O Nome Do Produto ? ')).strip()
    preco = float(input('Qual O Preço Do Produto? R$'))
    resp =  str(input('Você Deseja Finalizar Sua Compra? [S/N] ')).upper()
    soma = preco + soma 
    cont = cont +1
    if(cont==1):
        preco_barato = preco
        m_barato = nome
    else:
        if(preco_barato > preco):
            preco_barato = preco
            m_barato = nome
    if(preco > 1000):
        cont_1000 = cont_1000 + 1  
    if(resp == 'S'):
        print('\n\033[32mCompra Finalizada Com Sucesso!\033[m')
        print(f'O Preço Final Da Sua Compra É: R${soma} ')
        print(f'O Total De Produtos Que Custam Mais De R$1000 É De: {cont_1000}')
        print(f'O Produto Mais Barato Que Você Comprou Foi: {m_barato}')
        break