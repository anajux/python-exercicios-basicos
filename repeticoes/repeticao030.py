
'''O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
'''

def padaria(preço):
    
    print('Panificadora Pão de Ontem - Tabela de preços')
    for c in range (50):
        preçoPao = preço * (c+1)
        print(f'{c+1} - R$ {preçoPao:.1f}')
        
preço = float(input('Informe o preço do pão:'))
padaria(preço)
