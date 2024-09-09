# ItemPedido.py
from Produto import Produto

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self._produto = produto
        self._quantidade = quantidade

    @property
    def produto(self):
        return self._produto

    @property
    def quantidade(self):
        return self._quantidade
