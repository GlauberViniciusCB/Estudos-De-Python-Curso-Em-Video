# def linha ():
#     print('-' * 60)
# linha()
# print(f'{"Curso Em Video":^40}')
# linha()

# def mensagem (msg):
#     print('-'*30)
#     print(msg)
#     print('-'*30)
# mensagem('Sistema De Dados')

# def soma(a,b):
#     s = a + b    
#     print(s) 

# soma(4,5)
# soma(8,9)
# soma(2,1)
# def soma (a,b):
#     s = a + b
#     print(f'A Soma Do De A={a} E B={b} É {s}')
# soma(4,2)

# def contador(*num):
#     print(num)
# contador(3,4,7)
# contador(3,7)
# contador(13,2,27)

# def contador(*num):
#     tam = len(num)
#     print(f'Recebi Os Valores {num} São Um Total De {tam} Números.') 

# contador(3,7,8,2,1)
# contador(3,2)
# contador(10,8,2,1)

# def contador (*num):
#     for i in num:
#         print(i,end=' ')

# contador(2,37,88,9,0)

# def contador(*numero):
#     tam = len(numero)
#     for num in numero:
#         print(f'{num}', end=' ')
#     print(f'Foram Digitados Um Total De {tam} Números.')

# contador(2,7,55,9)

def dobra (valor):
    pos = 0
    while(pos < len(valor)):
        valor[pos] = valor[pos]*2
        pos = pos + 1
    print(valores)
valores=[2,7,5,8]
dobra (valores)
# print(valores)