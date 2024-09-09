
#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input('Insira um valor: '))

if numero > 0:
    print('{} é positivo!'.format(numero))
elif numero == 0:
    print('{} não é positivo nem negativo!'.format(numero))
else:
    print('{} é negativo!'.format(numero))
    
    