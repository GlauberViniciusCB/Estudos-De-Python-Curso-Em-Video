import math 
ang = float(input('Digite Um Angulo: '))
final= math.radians(ang)
print('O Seno Do Angulo {} É: {:.2f}'.format(ang,math.sin(final)))
print('O Cosseno Do Angulo {} É: {:.2f}'.format(ang,math.cos(final)))
print('O Tangente Do Angulo {} É {:.2f}'.format(ang,math.tan(final)))
