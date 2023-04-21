# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então 
# o empréstimo será negado.
valor = float(input('\033[33mQual O Valor Da Casa?\033[m R$'))
salario = float(input('\033[33mQual O Seu Salário?\033[m R$'))
tempo = int (input('\033[33mEm Quantos Anos Deseja Pagar?\033[m '))
porc =(salario * 0.30)
por_mes = (valor / tempo)/12
if (por_mes > porc):
    print('\033[31mEmprestimo Negado! Você Tem Um Salario De R${} E Sua Parcela Seria De R${:.2f}, Porém A Parcela Utrapassa Os 30% Do Seu Salário!\033[m'.format(salario,por_mes))
else:
    print('\033[32mEmprestimo Permitido! Você Vai Pagar Durante {} Anos, O Valor De R${:.2f} Por Mês. \033[m '.format(tempo,por_mes))

