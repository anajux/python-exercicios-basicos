
#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def inteiro(n):
    if n > 0:
        resultado = 'P'
    elif n == 0:
        resultado = 'Neutro'
    else:
        resultado = 'N'
    return resultado

n = int(input('Digite um valor inteiro: '))

print(inteiro(n))