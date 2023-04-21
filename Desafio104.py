# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só 
# que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
    num_int = str(input('Digite Um Número Inteiro: ')).strip()
    if(num_int.isnumeric()):
        num_int = int(num_int)
        print(f'O Número Digitado Foi: {num_int}')
    else:
        while True:
            print('Por Favor Digite Um Número.')
            num_int = str(input('Digite Um Número Inteiro: ')).strip()
            if(num_int.isnumeric()):
                break
    print(f'Você Digitou: O Número {num_int}')
    
leiaInt()