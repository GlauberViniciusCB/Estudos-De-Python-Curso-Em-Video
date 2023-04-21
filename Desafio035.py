# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
lado1 = float(input('Informe O Valor Do 1° Lado: '))
lado2 = float(input('Informe O Valor Do 2° Lado: '))
lado3 = float(input('Informe O Valor Do 3° Lado: '))


if (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
    print('\n\033[32mÉ Possível Formar Um Triângulo Com Está Combinação.\033[m')
else:
    print('\n\033[31mNão É Possível Forma Um Triângulo Com Está Combinação.\033[m')
