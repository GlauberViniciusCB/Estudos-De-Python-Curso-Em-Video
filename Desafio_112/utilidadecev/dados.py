def leiaDinheiro(din):
    valor = False
    while not valor:
        dinheiro = str(input(din)).strip().replace(',','.')
        if(dinheiro.isalpha() or  dinheiro == ''):
            print(f'Erro {dinheiro} Não É Válido.')
        else:
            valor = True
            return float(dinheiro)
        