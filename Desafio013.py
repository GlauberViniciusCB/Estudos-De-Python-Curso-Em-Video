#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Qual O Seu Salário ? R$'))
novo_salario = salario*0.15
final = salario + novo_salario
print('Com o Aumento Dos 15% De Salário, O Seu Novo Salário Será De: R${:.2f}  '.format(final)) 
