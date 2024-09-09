
#Faça um programa que pergunte o preço de três produtos e
#informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('1º produto: '))
produto2 = float(input('2º produto: '))
produto3 = float(input('3º produto: '))

maisBarato= min(produto1, produto2, produto3)

print(f'O produto mais barato é {maisBarato}')
