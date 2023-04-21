# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um 
# valor monetário formatado.

import moeda

dinheiro = float(input('Digite Um Valor: R$'))
print(f'O Valor De {moeda.moeda(dinheiro)} Com Acréscimo De 10% : {moeda.moeda(moeda.aumenta(dinheiro))}')
print(f'O Valor De {moeda.moeda(dinheiro)} Com Desconto De 30% : {moeda.moeda(moeda.diminuir(dinheiro))}')
print(f'O Dobro De {moeda.moeda(dinheiro)} É : {moeda.moeda(moeda.dobro(dinheiro))}')
print(f'A Metade De {moeda.moeda(dinheiro)} É: {moeda.moeda(moeda.metade(dinheiro))}')