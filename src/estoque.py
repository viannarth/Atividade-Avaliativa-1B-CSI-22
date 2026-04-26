from src.item import Item, Ingrediente, BebidaLata
from src.constantes import TipoItem

class Estoque:
    def __init__(self) -> None:
        self._estoque:dict[Item, int] = {}

    def consultarEstoqueLista(self) -> list[Item]:
        itens:list[Item] = [item for item in self._estoque]
        return itens
    
    def consultarEstoqueItem(self, nome_item:str) -> int:
        item = self._verificarItem(nome_item)
        return self._estoque[item]
    
    def _verificarItem(self, nome_item:str) -> Item | False:
        for item in self._estoque:
            if item.consultarNome() == nome_item:
                return item
        return False
    
    def estocarItem(self, tipo_item:TipoItem, nome_item:str, quantidade_estoque:int) -> None:
        item = self._verificarItem(nome_item)
        if not item:
            if tipo_item == TipoItem.INGREDIENTE:
                self._estoque[Ingrediente(nome_item)] = quantidade_estoque
            elif tipo_item == TipoItem.LATA:
                self._estoque[BebidaLata(nome_item)] = quantidade_estoque
        else: self._estoque[item] += quantidade_estoque

    def atualizarEstoqueItem(self, nome_item:str, quantidade_vendida:int) -> None:
        item = self._verificarItem(nome_item)
        self._estoque[item] -= quantidade_vendida
        if self.consultarEstoqueItem(nome_item) == 0: self._estoque.pop(item)
