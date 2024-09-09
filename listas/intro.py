
lista = []

while True:
    print()
    print('Escolha a opção desejada:')
    print()
    print('1. Adicionar item na lista.')
    print('2. Excluir item na lista.')
    print('3. Exibir produto mais caro.')
    print('4. Exibir produto mais barato')
    print('5. Exibir lista de compras completa.')
    print('6. Sair do menu.')
    print()
    op = int(input('Digite o número: '))
    
    #função para adicionar produto na lista:
    def adicionar(lista):
        nome = input('Insira o nome do produto que deseja adicionar: ')
        valor = float(input('Insira o valor do produto: '))
        lista.append({'nome': nome, 'valor': valor})
        print(f'{nome} adicionado com sucesso!')
    
    #função para remover produto na lista:
    def remover(lista):
        if len(lista) == 0:
            print('A lista de compras está vazia. Adicione um item selecionando a opção 1 do menu.')
            
        else:
            item = input('Insira o nome do produto que deseja remover: ')
            # Verificar se o item está presente na lista
            produtos_encontrados = [produto for produto in lista if produto['nome'] == item]

            if produtos_encontrados:
                # Remover todos os produtos com o mesmo nome
                lista[:] = [produto for produto in lista if produto['nome'] != item]
                print(f'{item} removido com sucesso!')
            else:
                print(f'{item} não existe na lista.')
                
    #função para exibir o produto mais barato da lista.
    def mais_barato(lista):
        if len(lista) == 0:
            print('A lista de compras está vazia. Adicione um item selecionando a opção 1 do menu.')
        else:
            produto_mais_barato = min([(item['valor'], item['nome']) for item in lista])
            print(f'Produto mais barato: {produto_mais_barato[1]} (R${produto_mais_barato[0]:.2f})')

    #função para exibir o produto mais caro da lista.
    def mais_caro(lista):
        if len(lista) == 0:
            print('A lista de compras está vazia. Adicione um item selecionando a opção 1 do menu.')
        else:
            produto_mais_caro = max([(item['valor'], item['nome']) for item in lista])
            print(f'Produto mais caro: {produto_mais_caro[1]} (R${produto_mais_caro[0]:.2f})')
            
    #função para exibir a lista de compras.
    def exibir(lista):
        if len(lista) == 0:
            print('A lista de compras está vazia. Adicione um item selecionando a opção 1 do menu.')
        else:
            print('Lista de compras: ')
            
            #list comprehension para a exibição da lista ocorrer de modo mais simples.
            [print(f'- {item["nome"]} (R${item["valor"]:.2f})') for item in lista]
    
    
    #chamada das funções:
    if op == 1:
        adicionar(lista)
        
    elif op == 2:
        remover(lista)
    
    elif op == 3:
        mais_caro(lista)
    
    elif op == 4:
        mais_barato(lista)
    
    elif op == 5:
        exibir(lista)
    
    elif op == 6:
        print('Encerrando a aplicação... ')
        break
    else:
        print('Número Inválido.')

        
                
    