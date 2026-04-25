from src.constantes import TipoBebida, Doses, PRECO_BEBIDA_DOSADA, PRECO_BEBIDA_LATA
from abc import ABC


class Item(ABC):
    def __init__(self, nome:str) -> None:
        self._nome:str = nome

    def consultarNome(self) -> str:
        return self._nome

class Ingrediente(Item):
    def __init__(self, nome:str) -> None:
        super().__init__(nome)


class Bebida(ABC):
    def __init__(self, preco:int, tipo_bebida:TipoBebida) -> None:
        self._preco:int = preco
        self._tipo_bebida:TipoBebida = tipo_bebida

    def consultarTipoBebida(self) -> TipoBebida:
        return self._tipo_bebida

    def consultarPreco(self) -> int:
        return self._preco


class BebidaLata(Item, Bebida):
    def __init__(self, nome:str, quantidade:int = 0) -> None:
        super(Item, self).__init__(nome)
        preco_lata:int = PRECO_BEBIDA_LATA
        super(Bebida, self).__init__(preco_lata, TipoBebida.LATA)


class BebidaDosada(Bebida):
    def __init__(self, ingredientes:list[Ingrediente], doses:list[Doses]) -> None:
        preco_dosada:int = PRECO_BEBIDA_DOSADA
        super(Bebida, self).__init__(preco_dosada, TipoBebida.DOSADA)
        self._bebida_dosada = (ingredientes, doses)
