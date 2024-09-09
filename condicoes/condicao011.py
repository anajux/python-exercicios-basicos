#
#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salarioAtual = float(input('Informe o salário atual: '))

if salarioAtual <= 280.00:
    percentual = '20% de aumento'
    valorDoAumento = (salarioAtual * 20/100)
    novoSalario = (salarioAtual * 20/100) + salarioAtual
    
elif salarioAtual >= 281.00 and salarioAtual <= 700.00:
    percentual = '15% de aumento.'
    valorDoAumento = (salarioAtual * 15/100)
    novoSalario = (salarioAtual * 15/100) + salarioAtual

elif salarioAtual >= 701.00 and salarioAtual <= 1500.00:
    percentual = '10% de aumento.'
    valorDoAumento = (salarioAtual * 10/100)
    novoSalario = (salarioAtual * 10/100) + salarioAtual

elif salarioAtual >= 1501.00:
    percentual = '5% de aumento.'
    valorDoAumento = (salarioAtual * 5/100)
    novoSalario = (salarioAtual * 5/100) + salarioAtual
    
print(f'Salário antes do aumento: {salarioAtual} reais.\nPercentual de aumento: {percentual}\nValor do aumento {valorDoAumento} reais.\nNovo salário: {novoSalario} reais.')
    