# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, 
# mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Camisa',25.40, 
             'Óculos',200,
             'Calça',75.89,
             'Pendrive 16G',35.40,
             'Tênis',120)
print('¨¨¨¨'*10)
print('{:^42}'.format('Lista De Produtos'))
print('¨¨¨¨'*10)
for i in range(0,len(produtos)):
    if(i % 2 == 0):
        print(f'{produtos[i]:.<30}',end='')
    else:   
        print(f' R${produtos[i]:>4.2f}')
