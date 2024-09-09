
#Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.

car = []
for c in range(0,10):
    letra = str(input('Digite uma letra: '))
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        car.append(letra)     
tamanho = len(car)
print(f'{tamanho} consoantes foram lidas. São elas: {car}')
