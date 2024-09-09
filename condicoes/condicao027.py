'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

def compras():
    if kilo <= 5:
        morango = 2.50 * kilo
        maça = 1.80 * kilo
    else:
        morango = 2.20 * kilo
        maca = 1.50 * kilo
    
    total = morango + maça
    return total

def fruteira(compras()):
    if kilo > 8 or valor > 25.00:
        valor = valor - 10/100
    return valor

for c in range(break)
    if