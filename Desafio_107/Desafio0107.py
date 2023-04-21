import moeda

dinheiro = float(input('Digite Um Valor: R$'))
print(f'O Valor De R${dinheiro} Com Acréscimo De 10% : R${moeda.aumenta(dinheiro)}')
print(f'O Valor De R${dinheiro} Com Desconto De 30% : R${moeda.diminuir(dinheiro)}')
print(f'O Dobro De R${dinheiro} É : R${moeda.dobro(dinheiro)}')
print(f'A Metade De R${dinheiro} É: R${moeda.metade(dinheiro)}')
