from src.constantes import TipoBebida
from src.estoque import Item, Bebida
from src.carrinho import Carrinho

class MaquinaVendas(): 
    def __init__(self) -> None:
        self._estoque:dict[Item, int] = {}
        self._vendas:dict[TipoBebida, float] = {}

    def consultarSaldo(self) -> float:
        saldo = 0
        for tipo in self._vendas:
            saldo += self._vendas[tipo]
        return saldo

    def consultarEstoque(self) -> dict[Item, int]:
        return self._estoque

    def consultarEstoqueItem(self, item:Item) -> int:
        return self._estoque[item]

    def consultarValorBebida(self, tipo_bebida:TipoBebida) -> float:
        return self._vendas[tipo_bebida]

    def atualizarVendas(self, bebida:Bebida, quantidade_vendida:int) -> None:
        self._vendas[bebida.consultarTipoBebida()] += bebida.consultarPreco()*quantidade_vendida
        self._estoque[bebida] -= quantidade_vendida

    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        pass

    def realizarVenda(self, carrinho:Carrinho, bebida:Bebida, quantidade_vendida:int = 1) -> None:
        pass