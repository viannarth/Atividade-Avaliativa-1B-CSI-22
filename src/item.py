from src.constantes import TipoItem, TipoBebida, Doses, PRECO_BEBIDA_DOSADA, PRECO_BEBIDA_LATA
from abc import ABC

class Item(ABC):
    def __init__(self, nome:str, tipo_item:TipoItem) -> None:
        """!
        @brief Inicializa um item especifico
        @param nome Nome do item
        @param tipo_item Tipo do item
        """
        self._nome:str = nome
        self._tipo_item:TipoItem = tipo_item

    def consultarNome(self) -> str:
        """!
        @brief Consulta o nome do item
        @return Nome do item
        """
        return self._nome
    
    def consultarTipoItem(self) -> TipoItem:
        return self._tipo_item


class Ingrediente(Item):
    """!
    @brief Um ingrediente seria um tipo especifico de item. Foi-se criada uma outra classe para explicitar isso
    """
    def __init__(self, nome:str) -> None:
        """"!
        @brief Inicializa um item especifico ao chamar o construtuor da classe Item com o tipo sendo INGREDIENTE
        """
        super().__init__(nome, TipoItem.INGREDIENTE)


class Bebida(ABC):
    """!
    @brief Define uma classe abstrata de bebida
    """
    def __init__(self, preco:int, tipo_bebida:TipoBebida) -> None:
        """"!
        @brief inicializador
        @param _preco Preco do bebida
        @param _tipo_bebida Tipo da bebida
        """
        self._preco:int = preco
        self._tipo_bebida:TipoBebida = tipo_bebida

    def consultarTipoBebida(self) -> TipoBebida:
        """!
        @brief Consulta o tipo de bebida
        @return Tipo de bebida
        """
        return self._tipo_bebida

    def consultarPreco(self) -> int:
        """!
        @brief consulta o preco da bebida
        @return Preco da bebida
        """
        return self._preco


class BebidaLata(Item, Bebida):
    """!
    @brief Classe que herda de bebida e item
    """
    def __init__(self, nome:str) -> None:
        """!
        @brief Inicializa chamando os inicilizadores pai e definindo o preco da bebida
        @param nome Nome do bebida
        """
        preco_lata:int = PRECO_BEBIDA_LATA
        Item.__init__(self, nome, TipoItem.LATA)
        Bebida.__init__(self, preco_lata, TipoBebida.LATA)


class BebidaDosada(Bebida):
    """!
    @brief Classe que herda de Bebida
    """
    def __init__(self, agua:Ingrediente) -> None:
        """!
        @brief Inicializa chamando o inicilizador pai definindo o preco da bebida e criando um dicionario relacionando
        seus ingredientes com suas doses
        """
        preco_dosada:int = PRECO_BEBIDA_DOSADA
        super().__init__(preco_dosada, TipoBebida.DOSADA)
        self._bebida_dosada: dict[Ingrediente, Doses] = {agua: Doses.AGUA}

    def consultarIngredientes(self) -> dict[Ingrediente, Doses]:
        return self._bebida_dosada
    
    def adicionarIngrediente(self, ingrediente:Ingrediente, dose:Doses) -> None:
        """!
        @brief Adiciona um ingrediente a bebida dosada em questao
        @param ingrediente Ingrediente a ser adicionado
        @param dose dose a ser adicionada
        """
        self._bebida_dosada[ingrediente] = dose
