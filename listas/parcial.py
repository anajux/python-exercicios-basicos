#importação da classe para usar a função parcial.
from functools import partial

#função para converter a temperatura. 
def converter_temperatura(temp, escala='Celsius'):
    if escala == 'Celsius':
        return (temp * 9/5) + 32
    elif escala == 'Fahrenheit':
        return (temp - 32) * 5/9

#função parcial.
celsius_para_fahrenheit = partial(converter_temperatura, escala='Celsius')
fahrenheit_para_celsius = partial(converter_temperatura, escala='Fahrenheit')

#uso da função parcial para converter para Fahrenheit.
temp_celsius = 20
temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)

print(f'{temp_celsius} graus Celsius é igual a {temp_fahrenheit:.2f} graus Fahrenheit.')

#uso da função parcial para converter para Celsius.
temp_fahrenheit = 90
temp_celsius = fahrenheit_para_celsius(temp_fahrenheit)

print(f'{temp_fahrenheit} graus Fahrenheit é igual a {temp_celsius:.2f} graus Celsius.')
