
# Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimir(n):
    for c in range(n+1):
       linha = ' '.join([str(c)] * c)
       print(linha)

n = int(input('Informe um inteiro: '))
imprimir(n)
        
