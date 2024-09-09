
#Faça um programa que leia 5 números e informe a soma e a média dos números.

num = []
for c in range(0,5):
    numero = int(input('Informe um número: '))
    num.append(numero)
    
soma = sum(num)
media = soma / 5

print(f'A soma é {soma} e a média é {media}')

