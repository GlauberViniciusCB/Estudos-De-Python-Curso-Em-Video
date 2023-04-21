# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


lado1 = float(input('\033[33mInforme O Valor Do Lado 1\033[m: '))
lado2 = float(input('\033[33mInforme O Valor Do Lado 2\033[m: '))
lado3 = float(input('\033[33mInforme O Valor Do Lado 3\033[m: '))

if( lado2 + lado3 > lado1 and lado1 + lado3 > lado2 and lado1 + lado2 > lado3):
    print('\033[32mFormam Um Triângulo.\033[m')
    if(lado1==lado2==lado3):
        print('\033[33mDo Tipo Equilatero.\033[m')
    elif(lado1!=lado3!=lado2!=lado1):
        print('\033[33mDo Tipo Escaleno\033[m')
    else:
         print('\033[33mDo Tipo Isociles.\033[m')
else:
    print('\033[31mNão Formam Um Triangulo.\033[m')


