
'''Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.'''


nome = str(input('Digite seu nome: '))

for c in range(len(nome), 0, -1):
    print(nome[:c])