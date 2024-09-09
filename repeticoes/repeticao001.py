
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido.

numero = int(input('Digite uma nota de 0 a 10: '))
while numero > 10:
    print('Nota inválida, tente novamente.')
    numero = int(input('Digite uma nota de 0 a 10: '))