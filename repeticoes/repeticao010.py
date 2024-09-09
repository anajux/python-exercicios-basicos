
#Faça um programa que receba dois
# números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe um número: '))
intervalo = list()

for c in range(numero1, numero2 - 1):
    c += 1 
    intervalo.append(c)
    
print(intervalo)
