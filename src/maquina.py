from src.constantes import TipoBebida
from src.estoque import Item, Bebida, BebidaDosada, BebidaLata
from src.carrinho import Carrinho

class MaquinaVendas(): 
    def __init__(self) -> None:
        self.__estoque:dict[Item, int] = {}
        self.__vendas:dict[TipoBebida, float] = {}

    def consultarSaldo(self) -> float:
        saldo = 0
        for tipo in self.__vendas:
            saldo += self.__vendas[tipo]
        return saldo

    def consultarEstoque(self) -> dict[Item, int]:
        return self.__estoque

    def consultarEstoqueItem(self, item:Item) -> int:
        return self.__estoque[item]

    def consultarValorBebida(self, tipo_bebida:TipoBebida) -> float:
        return self.__vendas[tipo_bebida]

    def atualizarVendas(self, bebida:Bebida, quantidade_vendida:int) -> None:
        self.__vendas[bebida.consultarTipoBebida()] += bebida.consultarPreco()*quantidade_vendida
        self.__estoque[bebida] -= quantidade_vendida

    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        pass

    def realizarVenda(self, carrinho:Carrinho, bebida:Bebida, quantidade_vendida:int = 1) -> None:
        pass