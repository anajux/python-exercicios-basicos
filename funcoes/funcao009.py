
#Reverso do número.
# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(n):
    numero = int(str(n)[::-1])
    print(f'O número invertido é: {numero:02d}')
    return numero

n = int(input('Informe um número: '))
reverso(n)
    

