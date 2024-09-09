
'''Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
'''

def desenhar_retangulo(linhas=1, colunas=1):
    # Verifica se os valores estão dentro da faixa permitida
    linhas = max(1, min(20, linhas))
    colunas = max(1, min(20, colunas))
    
    # Desenha a parte superior do retângulo
    print('+' + '-' * (colunas - 2) + '+')
    
    # Desenha as linhas do meio
    for _ in range(linhas - 2):
        print('|' + ' ' * (colunas - 2) + '|')
    
    # Desenha a parte inferior do retângulo
    if linhas > 1:
        print('+' + '-' * (colunas - 2) + '+')

# Exemplo de uso da função
desenhar_retangulo(5, 10)

