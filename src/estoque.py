from src.item import Item


class Estoque():
    def __init__(self) -> None:
        self._estoque:dict[Item, int] = {}

    def consultarEstoqueLista(self) -> dict[Item, int]:
        itens:list[Item] = [item for item in self._estoque]
        return itens
    
    def consultarEstoqueItem(self, item:Item) -> int:
        return self._estoque[item]
    
    def verificarItem(self, nome:str) -> Item | False:
        for item in self._estoque:
            if item.consultarNome() == nome:
                return item
        return False
    
    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        if self.consultarEstoqueItem(item) == 0: self._estoque[item] = quantidade_estoque
        else :self._estoque[item] += quantidade_estoque

    def atualizarEstoqueItem(self, item:Item, quantidade_vendida:int) -> None:
        self._estoque[item] -= quantidade_vendida
        if self.consultarEstoqueItem(item) == 0: self._estoque.pop(item)
