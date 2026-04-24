from src.constantes import TipoBebida, Doses, PRECO_BEBIDA_DOSADA, PRECO_BEBIDA_LATA
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nome:str, quantidade:int) -> None:
        self._nome:str = nome
        self._quantidade:int = quantidade

    def consultarNome(self) -> str:
        return self._nome

    def consultarQuantidade(self) -> int:
        return self._quantidade

    @abstractmethod
    def atualizarQuantidade(self) -> None: 
        pass


class Ingrediente(Item):
    def __init__(self, nome:str, quantidade:int = 0) -> None:
        super().__init__(nome, quantidade)

    def atualizarQuantidade(self, delta_massa:int) -> None:
        self._quantidade += delta_massa


class Bebida(ABC):
    def __init__(self, preco:float, tipo_bebida:TipoBebida) -> None:
        self._preco:float = preco
        self._tipo_bebida:TipoBebida = tipo_bebida

    def consultarTipoBebida(self) -> TipoBebida:
        return self._tipo_bebida

    def consultarPreco(self) -> float:
        return self._preco


class BebidaLata(Item, Bebida):
    def __init__(self, nome:str, quantidade:int = 0) -> None:
        super(Item, self).__init__(nome, quantidade)
        preco_lata:float = PRECO_BEBIDA_LATA
        super(Bebida, self).__init__(preco_lata, TipoBebida.LATA)
        
    def atualizarQuantidade(self, delta_unidades:int) -> None:
        self._quantidade += delta_unidades


class BebidaDosada(Bebida):
    def __init__(self) -> None:
        preco_dosada:float = PRECO_BEBIDA_DOSADA
        super(Bebida, self).__init__(preco_dosada, TipoBebida.DOSADA)

    def criarBebidaDosada(self, agua:Ingrediente, ingredientes:list[Ingrediente], doses:list[Doses]) -> None:
        pass
