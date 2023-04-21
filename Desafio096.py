# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e 
# comprimento) e mostre a área do terreno.
def area():
    bas = float(input('Digite A Largura: '))
    alt = float(input('Digite A Altura: ')) 
    total = bas * alt
    print(f'A Area Total: {total}m²')

area() 

