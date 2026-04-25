from inspect import isclass

from src.constantes import TipoBebida
from src.estoque import Item, Bebida
from src.carrinho import Carrinho

class MaquinaVendas(): 
    def __init__(self) -> None:
        self._carrinho:Carrinho = Carrinho()
        self._estoque:dict[Item, int] = {}
        self._vendas:dict[TipoBebida, int] = {}

    def consultarSaldo(self) -> int:
        saldo = 0
        for tipo_bebida in self._vendas:
            saldo += self._vendas[tipo_bebida]
        return saldo
    
    def consultarSaldoBebida(self, tipo_bebida:TipoBebida) -> int:
        return self._vendas[tipo_bebida]

    def consultarEstoque(self) -> dict[Item, int]:
        return self._estoque

    def consultarEstoqueItem(self, item:Item) -> int:
        return self._estoque[item]

    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        pass

    def atualizarEstoqueItem(self, item:Item, quantidade_vendida:int = 1) -> None:
        pass

    def atualizarVendas(self, bebida:Bebida, quantidade_vendida:int) -> None:
        self._vendas[bebida.consultarTipoBebida()] += bebida.consultarPreco()*quantidade_vendida
        if (bebida.consultarTipoBebida() == TipoBebida.LATA):


    def realizarVenda(self) -> None:
        pass
