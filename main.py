#TODO: create a file for constants (prices for itens)
#TODO: create a .env file for allow private access
#TODO: separate the project in files

from abc import ABC, abstractmethod
from enum import Enum

class TipoBebida(Enum):
    LATA = 1
    DOSADA = 2


class Item(ABC):
    def __init__(self, nome:str, quantidade:int) -> None:
        self._nome:str = nome
        self._quantidade:int = quantidade

    def consultarNome(self) -> str:
        pass

    def consultarQuantidade(self) -> int:
        pass

    @abstractmethod
    def atualizarQuantidade(self) -> None: 
        pass


class Ingrediente(Item):
    def __init__(self, nome:str, quantidade:int = 0) -> None:
        super().__init__(nome, quantidade)

    def atualizarQuantidade(self, massa_usada:int) -> None:
        pass


class Bebida(ABC):
    def __init__(self, preco:float, tipo_bebida:TipoBebida) -> None:
        self._preco:float = preco
        self._tipo_bebida:TipoBebida = tipo_bebida

    def consultarTipoBebida(self) -> TipoBebida:
        pass

    def consultarPreco(self) -> float:
        pass


class BebidaLata(Item, Bebida):
    def __init__(self, nome:str, quantidade:int = 0) -> None:
        super(Item, self).__init__(nome, quantidade)
        preco_lata:float = 5.0
        super(Bebida, self).__init__(preco_lata, TipoBebida.LATA)
        
    def atualizarQuantidade(self, unidades_vendidas:int) -> None:
        pass


class Doses(Enum):
    TRINTA: 0.30
    CINQUENTA: 0.50
    SETENTA: 0.70
    CEM: 1.00


class BebidaDosada(Bebida):
    def __init__(self) -> None:
        preco_dosada:float = 10.0
        super(Bebida, self).__init__(preco_dosada, TipoBebida.DOSADA)

    def criarBebidaDosada(self, agua:Ingrediente, ingredientes:list[Ingrediente], doses:list[Doses]) -> None:
        pass


class FormaPagamento(Enum):
    PIX = 1
    DEBITO = 2
    CREDITO = 3


class Carrinho():
    def __init__(self) -> None:
        self.__carrinho:list[Bebida] = []
        self.__valor_total:float = 0
        self.__forma_pagamento:FormaPagamento = None

    def consultarBebidas(self) -> None:
        pass
    
    def consultarValorTotal(self) -> float:
        pass

    def definirFormaPagamento(self, forma_pagamento:FormaPagamento) -> None:
        pass

    def adicionarBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        pass


class MaquinaVendas(): 
    def __init__(self) -> None:
        self.__estoque:dict[Item, int] = {}
        self.__vendas:dict[Bebida, int] = {}
        self.__saldo:float = 0

    def consultarSaldo(self) -> float:
        pass

    def consultarEstoque(self) -> dict[Item, int]:
        pass

    def consultarEstoqueItem(self, item:Item) -> int:
        pass

    def consultarValorTotal(self) -> float:
        pass

    def consultarValorBebida(self, tipo_bebida:TipoBebida) -> float:
        pass

    def atualizarSaldo(self, bebida:Bebida, quantidade_vendida:int) -> None:
        pass

    def atualizarVendas(self, bebida:Bebida, quantidade_vendida:int) -> None:
        pass

    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        pass

    def realizarVenda(self, carrinho:Carrinho, bebida:Bebida, quantidade_vendida:int = 1) -> None:
        pass