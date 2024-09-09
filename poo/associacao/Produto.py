
class Produto:
    def __init__(self, codigo: int, valor: float, descricao: str) -> None:
        self._codigo: codigo
        self._valor: valor
        self._descricao: descricao
        
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def descricao(self):
        return self.descricao
    
    