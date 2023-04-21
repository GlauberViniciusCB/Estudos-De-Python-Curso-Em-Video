# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
# Ex: 
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~
def escreva(escrt):
    conta = len(escrt)+4
    print('~'*conta)
    print(f'  {escrt}')
    print('~'* conta)


escreva('Óla, Mundo!')
escreva('Glauber Vinicius')