
#Faça um programa que leia 5 números e informe o maior número.

numeros = list()
for c in range (0,5):
    num = int(input('Informe um número: '))
    numeros.append(num)

print(max(numeros))