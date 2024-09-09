
#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade = list()
altura = list()

for c in range (0,5):
    id = int(input('Informe a idade: '))
    idade.append(id)
    
    alt = float(input('Informe a altura: '))
    altura.append(alt)
    
idade.reverse()

altura.reverse()
print(f'Listas invertidas: {idade, altura}')