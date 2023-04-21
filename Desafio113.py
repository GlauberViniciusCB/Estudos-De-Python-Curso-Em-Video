# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de 
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(n_1):
    while True:
        try:
            numero = int(input(n_1).strip())
            return numero
        except:
            print(f'Erro, Não É Um Número Inteiro Tente Novamente.')
def leiaFloat(n_2):
    while True:
        try:
            numero = float(input(n_2).strip())
            return numero
        except:
            print(f'Erro, Não É Um Número Real Tente Novamente.') 
            

num_1 = leiaInt('Digite Um Número Inteiro: ')
num_2 = leiaFloat('Digite Um Número Real: ')
print(f'\nO Número Inteiro Digitado Foi {num_1} E O Número Real Digitado Foi {num_2}')