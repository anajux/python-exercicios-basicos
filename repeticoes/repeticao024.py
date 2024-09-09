
'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

nota = []

n = int(input('Quantas notas deseja inserir? '))

for c in range(0,n):
    notas = float(input(f'Insira a {c+1}º nota: '))
    nota.append(notas)

media = (sum(nota))/n

print(f'A média das notas é: {media}')


