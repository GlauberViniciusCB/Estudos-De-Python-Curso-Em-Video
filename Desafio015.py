# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Informe A Quantidade De Km Percorridos: ')) 
dia = int(input('Quantos Dias O Carro Ficou Alugado? ')) 
total = (60*dia) + (0.15*km)
print ('O Valor A Ser Pago Pelo Aluguel Do Carro É De: R$ {:.2f}'.format(total))
