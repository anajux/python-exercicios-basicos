
'''Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.'''

nome = str(input('Digite seu nome: '))

for c in range(len(nome)):
    print(nome[:c+1])