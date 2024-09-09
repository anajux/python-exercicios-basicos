
#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

numeros = []
pares = []
impar = []

for c in range(0,20):
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num%2 == 0:
        pares.append(num)
    else:
        impar.append(num)
        
print(f'Números: {numeros}\nPares: {pares}\nÍmpar: {impar}')
