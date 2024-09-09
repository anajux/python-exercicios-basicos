'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
lista = []

n = int(input('Informe quantos itens terá o conjunto: '))
for c in range(0,n):
    num = int(input(f'Informe o {c+1}º número: '))
    lista.append(num)
    
print(f'Na lista {lista}, o maior número é {max(lista)}, o menor número é {min(lista)} e o somatório de todos elementos é {sum(lista)}')    