from src.constantes import TipoItem, TipoBebida, Doses, PRECO_BEBIDA_DOSADA, PRECO_BEBIDA_LATA
from abc import ABC

class Item(ABC):
    def __init__(self, nome:str, tipo_item:TipoItem) -> None:
        self._nome:str = nome
        self._tipo_item:TipoItem = tipo_item

    def consultarNome(self) -> str:
        return self._nome
    
    def consultarTipoItem(self) -> TipoItem:
        return self._tipo_item


class Ingrediente(Item):
    def __init__(self, nome:str) -> None:
        super().__init__(nome, TipoItem.INGREDIENTE)


class Bebida(ABC):
    def __init__(self, preco:int, tipo_bebida:TipoBebida) -> None:
        self._preco:int = preco
        self._tipo_bebida:TipoBebida = tipo_bebida

    def consultarTipoBebida(self) -> TipoBebida:
        return self._tipo_bebida

    def consultarPreco(self) -> int:
        return self._preco


class BebidaLata(Item, Bebida):
    def __init__(self, nome:str) -> None:
        preco_lata:int = PRECO_BEBIDA_LATA
        Item.__init__(self, nome, TipoItem.LATA)
        Bebida.__init__(self, preco_lata, TipoBebida.LATA)


class BebidaDosada(Bebida):
    def __init__(self, agua:Ingrediente) -> None:
        preco_dosada:int = PRECO_BEBIDA_DOSADA
        super().__init__(preco_dosada, TipoBebida.DOSADA)
        self._bebida_dosada: dict[Ingrediente, Doses] = {agua: Doses.AGUA}

    def consultarIngredientes(self) -> dict[Ingrediente, Doses]:
        return self._bebida_dosada
    
    def adicionarIngrediente(self, ingrediente:Ingrediente, dose:Doses) -> None:
        self._bebida_dosada[ingrediente] = dose
