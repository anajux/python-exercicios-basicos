
'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"'''

def investigação():
    contagem = 0
    
    for c in range(1):
        vitima = str(input('Telefonou para a vítima? ')).lower()
        if vitima == 'sim' or vitima == 's':
            contagem += 1
            
        local = str(input('Esteve no local do crime? ')).lower()
        if local == 'sim' or local == 's':
            contagem += 1
            
        mora = str(input('Mora perto da vítima? ')).lower()
        if mora == 'sim' or mora == 's':
            contagem += 1
            
        devia = str (input('Devia para a vítima? ')).lower()
        if devia == 'sim' or devia == 's':
            contagem += 1
            
        trabalho = str(input('Já trabalhou com a vítima? ')).lower()
        if trabalho == 'sim' or trabalho == 's':
            contagem += 1
        
    if contagem == 2:
        print('Suspeita.')
    elif contagem == 3 or contagem == 4:
        print('Cúmplice.')
    elif contagem == 5:
        print('Assassino')
    else:
        print('Inocente')
  

print('Responda as perguntas a seguir com "SIM" ou "NÃO", também será aceito abreviaturas, como "S" ou "N"')
investigação()
