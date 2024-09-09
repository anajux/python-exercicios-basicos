
'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
'''
altura = []
peso = []
codigo = []

def senso():
    while True:
        cod = int(input('Digite o seu código: '))
        if cod == 0:
            break
        else:
            codigo.append(cod)
            alt = float(input('Digite a sua altura: '))
            altura.append(alt)
            pes = float(input('Digite o seu peso: '))
            peso.append(pes)
        
    maisAlto = max(altura)
    maisBaixo = min(altura)
    maisGordo = max(peso)
    maisMagro = min(peso)
    mediaAltura = sum(altura) / len(altura)
    mediaPeso = sum(peso) / len(peso)
    
    print(f'O cliente mais alto tem código {codigo[altura.index(maisAlto)]}, altura {maisAlto} metros e peso {peso[altura.index(maisAlto)]} kg.')
    print(f'O cliente mais baixo tem código {codigo[altura.index(maisBaixo)]}, altura {maisBaixo} metros e peso {peso[altura.index(maisBaixo)]} kg.')
    print(f'O cliente mais gordo tem código {codigo[peso.index(maisGordo)]}, altura {altura[peso.index(maisGordo)]} metros e peso {maisGordo} kg.')
    print(f'O cliente mais magro tem código {codigo[peso.index(maisMagro)]}, altura {altura[peso.index(maisMagro)]} metros e peso {maisMagro} kg.')
    print(f'Média das alturas: {mediaAltura:.2f} metros')
    print(f'Média dos pesos: {mediaPeso:.2f} kg')
    
senso()