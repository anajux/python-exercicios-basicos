
#Altere o programa anterior permitindo ao usuário informar as populações 
# e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


A = float(input('Digite a população de A: '))
while A == 0:
    print('Inválido, tente novamente.')
    A = float(input('Digite a população de A: '))
    
B = float(input('Digite a população de B: '))
while B == 0:
    print('Inválido, tente novamente.')
    B = float(input('Digite a população de B: '))
    
crescimentoA = float(input('Digite o percentual de crescimento de A: '))
while crescimentoA == 0:
    print('Inválido, tente novamente.')
    crescimentoA = float(input('Digite o percentual de crescimento de A: '))
    
crescimentoB = float(input('Digite o percentual de crescimento de B: '))
while crescimentoB == 0:
    print('Inválido, tente novamente.')
    crescimentoB = float(input('Digite o percentual de crescimento de B: '))
    
anos = 0
while A <= B:
    A += A * crescimentoA
    B += B * crescimentoB
    anos += 1

print(f'Vai levar {anos} anos.')
