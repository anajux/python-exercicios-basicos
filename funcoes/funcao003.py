
#Faça um programa, # com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.

def soma(a, b, c):
    soma = a+b+c
    return soma

a = int(input('Informe o primeiro número inteiro: '))
b = int(input('Informe o segundo número inteiro: '))
c = int(input('Informe o terceiro número inteiro: '))

resultado = soma(a,b,c)

print(f'O resultado da soma entre {a}, {b}, {c} é: {resultado}')