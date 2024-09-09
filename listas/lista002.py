
#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

num = []
for c in range(0,10):
    numero = int(input('Digite um número: '))
    num.append(numero)
    
num.reverse()
print(num)