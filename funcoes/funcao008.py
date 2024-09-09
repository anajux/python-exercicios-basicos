
# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def digitos(n):
    print(f'{n} tem {len(str(n))} digitos.')
    return n

n = int(input('Informe um número inteiro: '))
digitos(n)
