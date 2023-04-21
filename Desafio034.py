#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
#a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe O Seu Salário: R$'))
if (salario > 1250):
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print('Seu Aumento É De {}, E Seu Novo Salário É: {:.2f} '.format(aumento,novo_salario))
elif (salario <= 1250):
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print('Seu Aumento É De {}, E Seu Novo Salário É: {:.2f} '. format(aumento,novo_salario)) 

