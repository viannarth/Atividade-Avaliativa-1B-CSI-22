from src.item import Item


class Estoque():
    def __init__(self) -> None:
        self._estoque:dict[Item, int] = {}

    def consultarEstoque(self) -> dict[Item, int]:
        return self._estoque
    
    def consultarEstoqueItem(self, item:Item) -> int:
        if item not in self._estoque: return 0
        return self._estoque[item]
    
    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        if item not in self._estoque: self._estoque[item] = quantidade_estoque
        else :self._estoque[item] += quantidade_estoque

    def atualizarEstoqueItem(self, item:Item, quantidade_vendida:int) -> None:
        self._estoque[item] -= quantidade_vendida
        if self._estoque[item] == 0: del self._estoque[item]
