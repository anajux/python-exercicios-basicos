
'''Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.'''

import re
from collections import Counter

frase = str(input('Digite uma frase: ')).lower()
   
espaço = 0

for i in range(0, len(frase)):
    if frase[i] == " ":   
        espaço += 1

vogais = Counter(re.sub('[^aeiou]', '', frase))

for vogal, quantidade in vogais.items():
    print(f'A frase "{frase}" possui {espaço} espaço(s) e {quantidade} vogal(is) "{vogal}"')

