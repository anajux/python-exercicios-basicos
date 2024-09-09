
from ItemPedido import ItemPedido
from Produto import Produto
from typing import List

class Pedido:
    def __init__(self) -> None:
        self._lista: List[ItemPedido] = []

    def adicionar_item(self, item: ItemPedido) -> None:
        self._lista.append(item)

    def obter_total(self) -> float:
        valor_total = 0.0
        for item in self._lista:
            valor_total += item.produto.get_valor() * item.quantidade
        return valor_total


pr1 = Produto(123, 25.50, 'blusa')
ip1 = ItemPedido(pr1, 2)
ped1 = Pedido()
ped1.adicionar_item(ip1)
total = ped1.obter_total()
print(total)

        