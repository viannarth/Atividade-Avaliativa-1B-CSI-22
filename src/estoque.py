from src.item import Item, Ingrediente, BebidaLata
from src.constantes import TipoItem


class Estoque():
    """!
    @brief Define o Estoque atual na máquina, podendo ser modificado ao adicionar ou remover itens
    """
    def __init__(self) -> None:
        """!
        @brief Inicializa o Estoque atual
        @param _estoque Um dicionario contendo a quantidade de cada item
        """
        self._estoque:dict[Item, int] = {}

    def consultarEstoqueLista(self) -> list[Item]:
        """!
        @brief Consulta o Estoque atual
        @return Retorna uma lista de itens no estoque
        """
        itens:list[Item] = [item for item in self._estoque]
        return itens
    
    def consultarEstoqueItem(self, nome_item:str, tipo_item:TipoItem) -> int:
        item = self.verificarItem(nome_item, tipo_item)
        return self._estoque[item]
    
    def verificarItem(self, nome_item:str, tipo_item:TipoItem) -> Item | False:
        for item in self._estoque:
            if item.consultarNome() == nome_item and item.consultarTipoItem() == tipo_item:
                return item
        return False
    
    def estocarItem(self, tipo_item:TipoItem, nome_item:str, quantidade_estoque:int) -> None:
        item = self.verificarItem(nome_item, tipo_item)
        if not item:
            if tipo_item == TipoItem.INGREDIENTE:
                self._estoque[Ingrediente(nome_item)] = quantidade_estoque
            elif tipo_item == TipoItem.LATA:
                self._estoque[BebidaLata(nome_item)] = quantidade_estoque
        else: self._estoque[item] += quantidade_estoque

    def atualizarEstoqueItem(self, tipo_item:TipoItem, nome_item:str, quantidade_vendida:int) -> None:
        item = self.verificarItem(nome_item, tipo_item)
        self._estoque[item] -= quantidade_vendida
        if self.consultarEstoqueItem(nome_item, tipo_item) == 0: self._estoque.pop(item)
