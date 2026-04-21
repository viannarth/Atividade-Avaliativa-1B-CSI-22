from abc import ABC, abstractmethod
from padrao import TipoBebida, Doses

class Item(ABC):
    def __init__(self, nome:str, quantidade:int) -> None:
        self.__nome:str = nome
        self.__quantidade:int = quantidade

    def consultarNome(self) -> str:
        return self.__nome

    def consultarQuantidade(self) -> int:
        return self.__quantidade

    @abstractmethod
    def atualizarQuantidade(self) -> None: 
        pass


class Ingrediente(Item):
    def __init__(self, nome:str, quantidade:int = 0) -> None:
        super().__init__(nome, quantidade)

    def atualizarQuantidade(self, massa_usada:int) -> None:
        self.__quantidade = self.__quantidade - massa_usada


class Bebida(ABC):
    def __init__(self, preco:float, tipo_bebida:TipoBebida) -> None:
        self.__preco:float = preco
        self.__tipo_bebida:TipoBebida = tipo_bebida

    def consultarTipoBebida(self) -> TipoBebida:
        return self.__tipo_bebida

    def consultarPreco(self) -> float:
        return self.__preco


class BebidaLata(Item, Bebida):
    def __init__(self, nome:str, quantidade:int = 0) -> None:
        super(Item, self).__init__(nome, quantidade)
        preco_lata:float = 5.0
        super(Bebida, self).__init__(preco_lata, TipoBebida.LATA)
        
    def atualizarQuantidade(self, unidades_vendidas:int) -> None:
        self.__quantidade = self.__quantidade - unidades_vendidas


class BebidaDosada(Bebida):
    def __init__(self) -> None:
        preco_dosada:float = 10.0
        super(Bebida, self).__init__(preco_dosada, TipoBebida.DOSADA)

    def criarBebidaDosada(self, agua:Ingrediente, ingredientes:list[Ingrediente], doses:list[Doses]) -> None:
        pass