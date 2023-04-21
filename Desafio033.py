n1 = int (input('Digite O 1° Número: '))
n2 = int (input('Digite O 2° Número: '))
n3 = int (input('Digite O 3° Número: ')) 

if (n1>n2 and n1>n3):
    maior = n1 
elif (n2>n1 and n2>n3):
    maior = n2   
else:
    maior = n3
   


if (n1<n2 and n1<n3):
    menor = n1
elif (n2<n1 and n2<n3):
    menor = n2
else:
    menor = n3

print('O Maior Número É: {}'.format(maior))
print('O Menor Número É: {}'.format(menor))
