'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''

lista = []
pares = []
impares = []

for c in range(0,10):
    num = int(input(f'Informe o {c+1}º número: '))
    lista.append(num)
    
for items in lista:
    if items % 2 == 0:
        pares.append(items)
    else:
        impares.append(items)

print(f'Na lista {lista}, tem {len(pares)} números pares e {len(impares)} números impares')