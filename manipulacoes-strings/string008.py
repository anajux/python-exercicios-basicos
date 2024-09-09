
'''Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
'''
import re

espaço = ""
def remove(frase):
    espaço = re.sub(r'[^A-Za-z]', '', frase)
    return espaço


frase = str(input('Informe uma frase: ')).upper().strip()
espaço = remove(frase)
invertida = espaço[::-1]

if espaço == invertida:
    print(f'A frase {frase} é um palíndromo.')
else:
    print(f'A frase {frase} não é um palíndromo.')
