# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de 
# pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros
valor = float(input('\033[33mInforme O Valor Do Produto:\033[m R$ '))
print('\n\033[32m1 - Dinheiro/Cheque.''\n2 - Cartão.''\n3 - 2x No Cartão''\n4 - 3x Ou Mais No Cartão\033[m')
escolha = int(input('\n\033[34mQual Será  a Forma De Pagamento?\033[m '))


if (escolha == 1):
    total = valor * 0.10
    total = valor - total
    print('\nO Valor Da Sua Compra É De R${:.2f}, E Você Recebeu Um Desconto De 10% , O Valor Final A Pagar É: R${:.2f}'.format(valor,total))
elif (escolha == 2):
    total = valor * 0.05
    total = valor - total
    print('\nO Valor Da Sua Compra É De R${:.2f}, E Você Recebeu Um Desconto De 5% , O Valor Final A Pagar É: R${:.2f}'.format(valor,total))
elif(escolha == 3):
    total=valor
    print('\nO Valor Da Sua Compra É De R${:.2f}, Não Há Desconto, O Valor Final A Pagar É: R${:.2f}'.format(valor,total))
elif(escolha == 4):
    parcela = int (input('Quantas Vezes Deseja Pagar? '))
    total = valor * 0.20
    total = valor + total
    parcelas = total/parcela
    print('\n')
    print('\nO Valor Da Sua Compra É De R${:.2f}, E Você Recebeu Um Acrecimo De 20% , O Valor Final A Pagar É: R${:.2f} Em {} Parcelas De R${:.2f}'.format(valor,total,parcela,parcelas))
