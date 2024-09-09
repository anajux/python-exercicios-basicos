#Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade em estoque. 
# Adicione métodos para calcular o valor total em estoque e verificar se o produto está disponível.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade 

    def estoque(self):
        estoque = self.preco * self.quantidade
        return estoque

    def disponivel(self):
        if self.quantidade == 0:
            return 'Produto não disponível.'
        else:
            return f'Há {self.quantidade} produtos no estoque.'
            
p1 = Produto('feijão', 3.80, 10)
print(p1.estoque())
print(p1.disponivel())
print(p1.nome)
print(p1.preco)

p2 = Produto('arroz', 1.80, 100)
print(p2.estoque())
print(p2.disponivel())
print(p2.nome)
print(p2.preco)
