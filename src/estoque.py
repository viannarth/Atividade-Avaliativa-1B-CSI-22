from src.item import Item

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

    def consultarEstoque(self) -> dict[Item, int]:
        """!
        @brief Consulta o Estoque atual
        @return Retorna o dicionario contendo a quantidade de cada item
        """
        return self._estoque
    
    def consultarEstoqueItem(self, item:Item) -> int:
        """!
        @brief Consulta a quantidade de item especifico
        @param item Item que ser consultado
        @return Retorna o quantidade de um item especifico
        """
        if item not in self._estoque: return 0
        return self._estoque[item]
    
    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        """!
        @brief Coloca uma certa quantidade de um item especifico no estoque
        @param item Item a ser adicionado
        @param quantidade_estoque Quantidade do item a ser estocado
        """
        if self.consultarEstoque(item) == 0: self._estoque[item] = quantidade_estoque
        else :self._estoque[item] += quantidade_estoque

    def atualizarEstoqueItem(self, item:Item, quantidade_vendida:int) -> None:
        """!
        @brief Serve para reduzir a quantidade de um item no estoque ao realizar uma compra
        @param item Item a ser vendido
        @param quantidade_vendida Quantidade do item a ser vendida
        """
        self._estoque[item] -= quantidade_vendida
        if self.consultarEstoque(item) == 0: self._estoque.pop(item)
