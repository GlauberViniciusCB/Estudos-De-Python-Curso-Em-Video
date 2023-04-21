# help(print)
# print(input.__doc__)
# def somar(a=0,b=0,c=0):
#     s = a + b + c
#     return s

# r1 = somar(3,4,6)
# r2 = somar(3,6)
# r3 = somar(4)
# print(f'Os Resltados Calculados Foram: {r1} {r2} {r3}')

# def fatorial (numero):
#     fat =1
#     for num in range(numero,0,-1):
#         fat = fat * num  
#     return fat

# print(fatorial(5))

# def fatorial(n):
#     inicio = n 
#     fim = 0
#     fat = 1
#     while(inicio > fim):
#         fat = fat * inicio
#         inicio = inicio - 1   
#     return fat

# print(fatorial(5))

def Par(n = 0):
    if(n % 2 == 0):
        return('O Número Digitado É Par.')
    else:
        return('O Número Digitado É Impar.')

# print(Par(15))
num = int(input('Digite Um Número: '))
print(Par(num))