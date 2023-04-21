# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
def descri():
    while True:
        duvida = str(input('Digite Um Método Inteno E Veja Descrição Do Mesmo:  ').strip()).lower()
        if(duvida=='fim'):
            print('Programa Finalizado')
            break
        help(duvida)
        print(duvida)


descri()