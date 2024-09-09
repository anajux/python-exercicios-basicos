
#Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

inteiro = 0
for c in range(0,10):
    inteiro += int(input('Digite um número inteiro: ')) **2

print(f'A soma dos quadrados é: {inteiro}')
    
    