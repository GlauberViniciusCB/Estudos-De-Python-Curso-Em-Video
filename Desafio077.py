# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada 
# palavra, quais são as suas vogais.
palavras = ('caneta','computador','sol','lua','telefone','teclado')
print(palavras)
for palavra in palavras:
    print(f'\nA Palavra {palavra} Tem As Vogais: ',end='')
    for letra in palavra:
        if (letra in 'aeiou'):
            print(f'{letra}',end=' ')
