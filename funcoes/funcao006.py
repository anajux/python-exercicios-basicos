
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.



def converter(hora, minuto):
    if hora < 12:
        periodo = 'A.M'
        if hora == 0:
            hora = 12
    else:
        periodo = 'P.M'
        if hora != 12:
            hora -= 12
    return hora, minuto, periodo


def imprimir(hora, minuto, periodo):
    print(f'A hora convertida é: {hora}:{minuto:2d} {periodo}')
    
hora = int(input('Informe a hora: '))
minuto = int(input('Informe os minutos: '))
hora, minuto, periodo = converter(hora, minuto)
imprimir(hora, minuto, periodo)