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
    
    def consultarEstoqueItem(self, nome_item:str) -> int:
        """!
        @brief Consulta a quantidade de item especifico
        @param nome_item Nome do Item a ser consultado
        @return Retorna o quantidade de um item especifico
        """
        item = self.verificarItem(nome_item)
        return self._estoque[item]
    
    def verificarItem(self, nome_item:str) -> Item | False:
        for item in self._estoque:
            if item.consultarNome() == nome_item:
                return item
        return False
    
    def estocarItem(self, tipo_item:TipoItem, nome_item:str, quantidade_estoque:int) -> None:
        """!
        @brief Coloca uma certa quantidade de um item especifico no estoque
        @details se o item nao tiver no estoque voce o adicona com uma certa quantidade. Se ele ja estiver no estoque
        voce apenas adiciona uma certa quantidade desse  item. Sao utilizados diferentes metodos a depender se
        o item seria um ingrediente ou uma bebida em lata
        """
        item = self.verificarItem(nome_item)
        if not item:
            if tipo_item == TipoItem.INGREDIENTE:
                self._estoque[Ingrediente(nome_item)] = quantidade_estoque
            elif tipo_item == TipoItem.LATA:
                self._estoque[BebidaLata(nome_item)] = quantidade_estoque
        else: self._estoque[item] += quantidade_estoque

    def atualizarEstoqueItem(self, nome_item:str, quantidade_vendida:int) -> None:
        """!
        @brief Serve para reduzir a quantidade de um item no estoque ao realizar uma compra
        @param nome_item Item a ser vendido
        @param quantidade_vendida Quantidade do item a ser vendida
        """
        item = self.verificarItem(nome_item)
        self._estoque[item] -= quantidade_vendida
        if self.consultarEstoqueItem(nome_item) == 0: self._estoque.pop(item)
