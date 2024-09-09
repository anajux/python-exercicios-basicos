
#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo += imposto
    return custo

taxaImposto = float(input('Informe a taxa de imposto: '))
custo = float(input('Informe quanto custa o produto: '))

print(f'O valor de custo com o imposto sobre vendas é de {somaImposto(taxaImposto, custo)}')
    