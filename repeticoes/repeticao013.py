
'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.'''

base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))
resultado = 1

for c in range(0, expoente):
    resultado *= base 
    
print(f'{base} elevado a {expoente} é: {resultado}')