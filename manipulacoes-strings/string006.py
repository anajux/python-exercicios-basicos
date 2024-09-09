'''Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.'''


def meses(valor):
    meses = [' ', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return meses[valor]


def converte(data):
    dia, mes, ano = data.split('/')
    valor = int(mes)
    return '{} de {} de {}'.format(dia, meses(valor), ano)


data = input('Insira a sua data de nascimento (DD/MM/AAAA): ')
print(converte(data))