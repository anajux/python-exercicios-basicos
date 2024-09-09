
#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for c in range (0,4):
    nota = float(input(f'Informe a nota {c+1}: '))
    notas.append(nota)
    
soma = sum(notas)
media = soma / 4

print(f'Notas: {notas}\nSoma: {soma}\nMédia: {media}')
    