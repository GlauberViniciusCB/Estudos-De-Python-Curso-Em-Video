def fatorial(numero):
    fat = 1
    for n in range (numero,0,-1):
        fat= n * fat 
    return fat

def dobro(n):
    return n*2

def Triplo(n):
    return n*3

num = int(input('Digite Um Número E Descubra Seu Fatorial: '))
final = fatorial(num)
print(f'O Fatorial Do Número {num} É: {final}')
print(f'O Dobro Do Número {num} É: {dobro(num)}')
print(f'O Triplo Do Número {num} É: {Triplo(num)}')