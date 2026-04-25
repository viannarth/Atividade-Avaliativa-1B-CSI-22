from src.constantes import TipoBebida
from src.estoque import Estoque
from src.item import Item, Bebida
from src.carrinho import Carrinho

class MaquinaVendas(): 
    def __init__(self) -> None:
        self._carrinho:Carrinho = Carrinho()
        self._estoque:Estoque = Estoque()
        self._vendas:dict[TipoBebida, float] = {}

    def consultarSaldo(self) -> float:
        saldo = 0
        for tipo_bebida in self._vendas:
            saldo += self._vendas[tipo_bebida]
        return saldo
    
    def consultarSaldoBebida(self, tipo_bebida:TipoBebida) -> float:
        return self._vendas[tipo_bebida]

    def atualizarVendas(self, bebida:Bebida, quantidade_vendida:int) -> None:
        self._vendas[bebida.consultarTipoBebida()] += bebida.consultarPreco()*quantidade_vendida
        if (bebida.consultarTipoBebida() == TipoBebida.LATA):

    def realizarVenda(self) -> None:
        pass
