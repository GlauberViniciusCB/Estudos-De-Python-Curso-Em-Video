from math import hypot

catop = float(input('Digite O Cateto Oposto: '))
catad = float(input('Digite O Cateto Adjacente: '))
print('A Hipotenusa De {} E {} É: {:.2f}'.format(catop,catad,hypot(catop,catad)))