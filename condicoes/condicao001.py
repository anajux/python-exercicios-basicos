
#Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe um número: '))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}.')
elif numero1 == numero2:
    print('Os número são iguais.')
else:
    print(f'{numero2} é maior que {numero1}.')