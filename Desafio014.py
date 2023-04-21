#  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperatura = float (input('Informe A Temperatura Em °C Para Converte -la A Fahrenheit: ' ))
nova_temp = (temperatura*1.8)+32
print('A Conversão De {}°C Para Fahrenheit É: {}°F'.format(temperatura,nova_temp))