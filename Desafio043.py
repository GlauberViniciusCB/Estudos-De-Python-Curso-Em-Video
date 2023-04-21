#  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre 
#  seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Informe Seu Peso: '))
altura = float(input('Informe Sua Altura: '))

media = (peso/(altura)**2) 
print('Sua Média É: {:.2f}'.format(media))

if(media < 18.5):
    print('\033[35mAbaixo Do Peso.\033[m')
elif(media >= 18.5 and media<25):
    print('\033[32mPeso Ideal.\033[m')
elif(media >=25 and media < 30):
    print('\033[33mSobrepeso.\033[m')
elif(media >=30 and media < 40 ):
    print('\033[33mObesidade.\033[m')
else:
    print('\033[31mObesidade Mórbida.\033[m')