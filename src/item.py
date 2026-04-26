from src.constantes import TipoBebida, Doses, PRECO_BEBIDA_DOSADA, PRECO_BEBIDA_LATA
from abc import ABC


class Item(ABC):
    """!
    @brief Define um item especifico
    """
    def __init__(self, nome:str) -> None:
        """!
        @brief Inicializa um item especifico
        @param nome Nome do item
        @param _nome Nome do item
        """
        self._nome:str = nome

    def consultarNome(self) -> str:
        """!
        @brief Consulta o nome do item
        @return Nome do item
        """
        return self._nome

class Ingrediente(Item):
    """!
    @brief Um ingrediente seria um tipo especifico de item. Foi-se criada uma outra classe para explicitar isso
    """
    def __init__(self, nome:str) -> None:
        """"!
        @brief Inicializa um item especifico e chama o construtuor da classe Item
        """
        super().__init__(nome)


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
    @brief Classe que herda de bebida
    """
    def __init__(self, nome:str) -> None:
        """!
        @brief Inicializa chamando o inicilizador pai e definindo o preco da bebida
        @param nome Nome do bebida
        """
        super(Item, self).__init__(nome)
        preco_lata:int = PRECO_BEBIDA_LATA
        super(Bebida, self).__init__(preco_lata, TipoBebida.LATA)


class BebidaDosada(Bebida):
    """!
    @brief Classe que herda de bebida
    """
    def __init__(self) -> None:
        """!
        @brief Inicializa chamando o inicilizador pai e definindo o preco da bebida
        @param _bebida_dosada Um dicionario que associa cada ingrediente que compoe a bebida com sua dose
        """
        preco_dosada:int = PRECO_BEBIDA_DOSADA
        super(Bebida, self).__init__(preco_dosada, TipoBebida.DOSADA)
        self._bebida_dosada: dict[Ingrediente, Doses] = {}

    def consultarIngrediente(self) -> dict[Ingrediente,Doses]:
        """!
        @brief Consulta o preco da bebida
        @return Dicionario que contem os ingredientes com sua reespectivas doses
        """
        return self._bebida_dosada
    
    def adicionarIngrediente(self, ingrediente:Ingrediente, dose:Doses) -> None:
        """!
        @brief Adiciona um ingrediente a bebida dosada em questao
        @param ingrediente Ingrediente a ser adicionado
        @param dose dose a ser adicionada
        """
        self._bebida_dosada[ingrediente] = dose
