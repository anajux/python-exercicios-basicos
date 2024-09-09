
'''Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.'''

from random import sample

def embaralha(palavra):
    palavra_Embaralhada = sample(palavra, len(palavra))
    espaços = ''.join(palavra_Embaralhada)
    print(f'{palavra} embaralhado é {espaços}')
    return palavra_Embaralhada

palavra = str(input('Digite a palavra que deseja embaralhar: '))
embaralha(palavra)

