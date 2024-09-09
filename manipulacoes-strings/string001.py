
'''Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.'''

nome1 = str(input('Informe a primeira string: ')).upper().strip()
nome2 = str(input('Informe a segunda string: ')).upper().strip()
tamanho1 = len(nome1)
tamanho2 = len(nome2)

print(f'{nome1} = {tamanho1}\n{nome2} = {tamanho2}')
if nome1 == nome2:
    print('As duas strings são iguais.')

else:
    print('As duas strings são diferentes.')
    
    