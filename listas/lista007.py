
#Faça um Programa que leia um vetor de 5 números inteiros, 
# mostre a soma, a multiplicação e os números.

from math import prod

numeros = []
for c in range (0,5):
    num = int(input('Digite um número inteiro: '))
    numeros.append(num)
    

print(f'Números da lista: {numeros}\nSoma: {sum(numeros)}\nMultiplicação: {prod(numeros)}')
