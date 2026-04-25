from src.constantes import TipoBebida, Doses, PRECO_BEBIDA_DOSADA, PRECO_BEBIDA_LATA
from abc import ABC, abstractmethod

#TODO: remove attribute _quantidade and relationated methods from all classes 
# that have it
#TODO: separate Item from stock and create a new class Estoque to store the 
# quantitites of the itens

class Item(ABC):
    def __init__(self, nome:str, quantidade:int) -> None:
        self._nome:str = nome
        self._quantidade:int = quantidade

    def consultarNome(self) -> str:
        return self._nome

    def consultarQuantidade(self) -> int:
        return self._quantidade

    @abstractmethod
    def atualizarQuantidade(self, delta_quantidade:int) -> None:
        pass


class Ingrediente(Item):
    def __init__(self, nome:str, quantidade:int = 0) -> None:
        super().__init__(nome, quantidade)

    def atualizarQuantidade(self, delta_massa:int) -> None:
        self._quantidade += delta_massa


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
        super(Item, self).__init__(nome, quantidade)
        preco_lata:int = PRECO_BEBIDA_LATA
        super(Bebida, self).__init__(preco_lata, TipoBebida.LATA)
        
    def atualizarQuantidade(self, delta_unidades:int) -> None:
        self._quantidade += delta_unidades

#TODO: change implementation of BebidaDosada
class BebidaDosada(Bebida):
    def __init__(self, ingredientes:list[Ingrediente], doses:list[Doses]) -> None:
        preco_dosada:float = PRECO_BEBIDA_DOSADA
        super(Bebida, self).__init__(preco_dosada, TipoBebida.DOSADA)
        self._bebida_dosada = (ingredientes, doses)