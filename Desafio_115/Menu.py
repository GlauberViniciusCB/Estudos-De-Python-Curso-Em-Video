
def Menu():
    print('==='*10)
    print('{:^30}'.format('Menu Principal'))
    print('==='*10)
    print()
    print('1 - Ver Pessoas Cadastradas. ' )
    print('2 - Cadastrar Nova Pessoa. ')
    print('3 - Sair')
    while True:
        escolha = str(input('Faça Sua Escolha: '))
        try:
            if(escolha.isnumeric()):
                esc = int(escolha)
            if(esc == 1):
                print('==='*10)
                print('{:^30}' .format('Opção 1'))
                print('==='*10)
                with open("Cadastro_De_Pessoas.txt",'r') as arquivo:
                    print(arquivo.read())
                    arquivo.close()
            if(esc == 2):
                print('==='*10)
                print('{:^30}'.format('Opção 2'))
                print('==='*10)
                with open("Cadastro_De_Pessoas.txt",'a') as arquivo:
                    nome = str(input('Nome: '))
                    idade = int(input('Idade: ')) 
                    arquivo.write(f'\n{nome};{idade}')
                    arquivo.close()
            if(esc == 3):
                print('==='*10)
                print('{:^30}'.format('Opção 3'))
                print('\n{:^30}'.format('Sistema Finalizado'))
                print('==='*10)
                arquivo.close()
                break
        except(UnboundLocalError):
                print('Por Favor Digite Um Número Inteiro.')
                continue