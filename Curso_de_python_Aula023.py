try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: ')) 
    resultado = a/b
except ZeroDivisionError:
    print('Erro, Não É Possivel Dividir Por "0".')    
except (ValueError,TypeError):
    print('Erro, No Tipo De Dados Informados.')
except KeyboardInterrupt:
    print('\nO Usuário Não Quis Informar Os Dados.')
except Exception as erro:
    print(f'O Erro Encontrado Foi {erro.__cause__}')
else:
    print(f'O Resultado Final Da Divisão Entre {a} E {b} Tem Como Resultado: {resultado:.1f}')
finally:
    print('Programa Finalizado.')