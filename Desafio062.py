# Melhore o DESAFIO 61: PA, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele
# disser que quer mostrar 0 termos.
# Formula:  an= a1+(n-1)*r

a1 = int(input('Informe O 1° Termo: '))
razao = int(input('Informe A Razão: '))
quant_termos = int(input('Informe A Quantidade De Termos Que Você Deseja Ver: '))
ult_termo = a1+(quant_termos - 1)*razao
cont = a1 

while(cont < ult_termo):
    print(cont,end=' ')
    cont = cont + razao
print(cont,end=' ')
ult_termo = cont
fim_quant = razao *quant_termos
soma = ult_termo + fim_quant
while(quant_termos!=0):
    if(quant_termos!=0):
        quant_termos = int(input('\n A Quantidade De Termos Que Você Deseja Ver: '))
        fim_quant = razao * quant_termos
        soma = ult_termo + fim_quant
        while(ult_termo < soma):
            print(ult_termo+razao,end=' ')
            ult_termo = ult_termo + razao 
if(quant_termos == 0):
        print('Fim Da Execução .')
