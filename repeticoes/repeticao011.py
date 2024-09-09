
#Altere o programa anterior para mostrar no final a soma dos números.


numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe um número: '))
intervalo = list()

for c in range(numero1, numero2 - 1):
    c += 1 
    intervalo.append(c)
    
print(f'O intervalo é {intervalo}, e a soma é {sum(intervalo)}.')

