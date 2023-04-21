#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de 
#  números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
num = (randint(1,50),randint(0,50),randint(0,50),randint(0,50),randint(0,50))
print(num)
print(f'O Maior Número Da Tupla: {max(num)}')
print(f'O Menor Número Da Tupla: {min(num)}')