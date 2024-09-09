
'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

lista = []

n = int(input('Informe quantos itens terá o conjunto [0 até 1000]: '))
if n <= 0 or n > 1000:
    while True:
        print(f'{n} não é aceito. Por favor insira um número menor que 1000 e maior que 0')    
        n = int(input('Informe quantos itens terá o conjunto [0 até 1000]: '))
    
for c in range(0,n):
    num = int(input(f'Informe o {c+1}º número: '))
    lista.append(num)
    
print(f'Na lista {lista}, o maior número é {max(lista)}, o menor número é {min(lista)} e o somatório de todos elementos é {sum(lista)}')    