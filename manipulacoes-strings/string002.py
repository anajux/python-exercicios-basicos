
'''Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.'''

nome = str(input('Digite o seu nome utilizando letras maiusculos ou minusculas: ')).upper()
invertido = nome[::-1]

print(f'Seu nome invertido é: {invertido}')