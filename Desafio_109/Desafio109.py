# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.
import moeda

dinheiro = float(input('Digite Um Valor: R$'))
print(f'O Valor De {moeda.moeda(dinheiro)} Com Acréscimo De 10% : {(moeda.aumenta(dinheiro,True))}')
print(f'O Valor De {moeda.moeda(dinheiro)} Com Desconto De 30% : {(moeda.diminuir(dinheiro,True))}')
print(f'O Dobro De {moeda.moeda(dinheiro)} É : {(moeda.dobro(dinheiro,True))}')
print(f'A Metade De {moeda.moeda(dinheiro)} É: {(moeda.metade(dinheiro,True))}')